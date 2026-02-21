from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from Dominus.models import *
from django.forms import inlineformset_factory
from .forms import *
from .filters import *
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from io import BytesIO

import random

# Create your views here.
#class perfil:
    #def __init__(self,ip,usuario):
        #self.user=usuario
        #self.ip=ip

listau=[]
#def get_client_ip(request):
    #x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    #if x_forwarded_for:
    #    ip = x_forwarded_for.split(',')[0]
    #else:
    #    ip = request.META.get('REMOTE_ADDR')
    #return ip
def registro(request):
    form = UserCreationForm()
    contexto={'form':form}
    return render(request, 'cuentas/registro.html',contexto)

def login(request):
    pass
def proveedores(request):
    proveedores = Proveedor.objects.all()
    ppfiltro = ProveedoresFiltro(request.GET, queryset=proveedores)

    proveedores = ppfiltro.qs
    return render(request, 'cuentas/proveedores.html', {'proveedores': proveedores,'ppfiltro':ppfiltro})
def empleados(request):
    empleados = Empleado.objects.all()
    efiltro = EmpleadosFiltro(request.GET, queryset=empleados)

    empleados = efiltro.qs
    return render(request, 'cuentas/empleados.html', {'empleados': empleados,'efiltro':efiltro})

def inicio(request):




    ordenes=Orden.objects.all()
    clientes= Cliente.objects.all()
    totalclientes= clientes.count()
    totalordenes = ordenes.count()
    devueltas=ordenes.filter(estado='Devuelto').count()

    enviadas=ordenes.filter(estado='Enviado').count()
    pendientes= ordenes.filter(estado='Pendiente').count()

    contexto={'ordenes':ordenes[:5],'clientes':clientes[:5],'totalordenes':totalordenes,'totalclientes':totalclientes,'enviadas':enviadas,
              'pendientes':pendientes,'devueltas':devueltas}
    return render(request, 'cuentas/dashboard.html',contexto)

def mclientes(request):
    clientes = Cliente.objects.order_by('idc')

    cfiltro = ClientesFiltro(request.GET, queryset=clientes)

    clientes = cfiltro.qs
    return render(request, 'cuentas/clientes.html', {'clientes': clientes, 'cfiltro': cfiltro})


def productos(request):

    productos = Inventario1.objects.order_by('codigo')

    pfiltro = ProductosFiltro(request.GET, queryset=productos)

    productos = pfiltro.qs
    return render(request, 'cuentas/productos.html', {'productos':productos,'pfiltro':pfiltro})


def login(request):

        return render(request,'cuentas/login.html')


def cerrar(request):
    return redirect('/')
    #global listau

    #for i in listau:
        #if i.ip == get_client_ip(request):
           # listau.pop(listau.index(i))

        #return redirect('/')

def factura(request,fct):

    ordns= fct
    prds=Inventario1.objects.all()
    ordenes=Orden.objects.filter(idf=ordns)
    cliente= Cliente.objects.get(idc=ordenes[0].cliente.idc)
    ords=[]
    for i in ordenes:
        if i.producto.descripcion not in ords:
            ords.append(i.producto.descripcion)
    contexto = {'idf': ordns,'fecha':ordenes[0].fecha,'orden':ordenes,'cliente':cliente,'dics':''}
    vld=[]
    total=0
    for a in ords:
        vls=prds.get(descripcion=a)
        vlc=ordenes.filter(producto__descripcion=vls.descripcion).count()
        vld.append({'nombre':vls.descripcion,'idpp':vls.id,'idp':vls.idp.nombre,'cant':vlc,'precio':vls.precioitbis,'total':vls.precioitbis*vlc})
    for b in vld:
        total+=b['total']
    contexto = {'idf': ordns, 'fecha': ordenes[0].fecha, 'orden': ordenes, 'cliente': cliente, 'dics': vld,'total':total,'totali':total*0.18,'totalit':total*1.18}
    return render(request,'cuentas/factura.html',contexto)

def facturas(request,pk):
    a=Orden.objects.filter(cliente_id=pk)

    d=Diario.objects.filter(cliente_id=pk,detalle='Devolucion')
    j=[]

    nota=[]
    for i in a:
       if  i.estado=='Devuelto':
        nota.append(i.idf)
       if i.idf not in j:
            j.append(i.idf)
    contexto={'facts':j,'notas':nota}
    return render(request, 'cuentas/facturas.html',contexto)
def cliente(request,pk_test):

    cliente=Cliente.objects.get(idc=pk_test)

    ordenes = cliente.orden_set.all()


    ordenescuenta = ordenes.count()

    miFiltro = OrdenFilter(request.GET, queryset=ordenes)

    ordenes = miFiltro.qs
    contexto={'cliente':cliente,'miFiltro':miFiltro, 'ordenes':ordenes,'ordenescuenta':ordenescuenta}
    return render(request, 'cuentas/cliente.html', contexto)
def ordenes(request):



    ordenes = Orden.objects.all()




    miFiltro = OrdenFilter(request.GET, queryset=ordenes)

    ordenes = miFiltro.qs
    contexto={'miFiltro':miFiltro, 'ordenes':ordenes}
    return render(request, 'cuentas/ordenes.html', contexto)



def crearCliente(request):

    form = clienteform()
    if request.method == 'POST':
        form = clienteform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    contexto = {'form': form}
    return render(request, 'cuentas/form_cliente.html', contexto)
def modCliente(request, pk):

    cliente= Cliente.objects.get(idc=pk)
    form= clienteform(instance=cliente)
    if request.method =='POST':
        form = ordenar(request.POST, instance=clienteform)
        if form.is_valid():
            form.save()
            return redirect('/')
    contexto={'form':form}
    return render(request, 'cuentas/form_cliente.html', contexto)
def borrarCliente(request, pk):



    cliente = Cliente.objects.get(idc=pk)

    if request.method=='POST':
        cliente.delete()
        return redirect('/')
    context = {'item': cliente}
    return render(request, 'cuentas/deleteC.html', context)
def crearProd(request):

    form = productoform()
    if request.method == 'POST':
        form = productoform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    contexto = {'form': form}
    return render(request, 'cuentas/form_producto.html', contexto)
def modProd(request, pk):

    producto= Cliente.objects.get(idc=pk)
    form= productoform(instance=producto)
    if request.method =='POST':
        form = productoform(request.POST, instance=productoform)
        if form.is_valid():
            form.save()
            return redirect('/')
    contexto={'form':form}
    return render(request, 'cuentas/form_producto.html', contexto)
def borrarProd(request, pk):



    producto = Inventario1.objects.get(id=pk)

    if request.method=='POST':
        producto.delete()
        return redirect('/')
    context = {'item': producto}
    return render(request, 'cuentas/deletePROD.html', context)
def crearProv(request):

    form = proveedorform()
    if request.method == 'POST':
        form = proveedorform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    contexto = {'form': form}
    return render(request, 'cuentas/form_proveedor.html', contexto)
def modProv(request, pk):

    proveedor= Proveedor.objects.get(idp=pk)
    form= proveedorform(instance=proveedor)
    if request.method =='POST':
        form = proveedorform(request.POST, instance=proveedorform)
        if form.is_valid():
            form.save()
            return redirect('/')
    contexto={'form':form}
    return render(request, 'cuentas/form_proveedor.html', contexto)
def borrarProv(request, pk):



    proveedor = Proveedor.objects.get(idp=pk)

    if request.method=='POST':
        proveedor.delete()
        return redirect('/')
    context = {'item': proveedor}
    return render(request, 'cuentas/deletePROV.html', context)
def crearEmpl(request):

    form = empleadoform()
    if request.method == 'POST':
        form = empleadoform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    contexto = {'form': form}
    return render(request, 'cuentas/form_empleado.html', contexto)
def modEmpl(request, pk):

    empleado= Empleado.objects.get(numemp=pk)
    form= empleadoform(instance=empleado)
    if request.method =='POST':
        form = empleadoform(request.POST, instance=empleadoform)
        if form.is_valid():
            form.save()
            return redirect('/')
    contexto={'form':form}
    return render(request, 'cuentas/form_empleado.html', contexto)
def borrarEmpl(request, pk):



    empleado = Empleado.objects.get(numemp=pk)

    if request.method=='POST':
        empleado.delete()
        return redirect('/')
    context = {'item': empleado}
    return render(request, 'cuentas/deleteEMPL.html', context)

extra=1
def crearOrden(request, pk):
    global extra
    if request.method!='POST':
        extra=1
        ordenarSet = inlineformset_factory(Cliente, Orden, fields=('producto','estado','nota'), extra=extra)
        cliente= Cliente.objects.get(idc=pk)
        formularioset=ordenarSet(queryset=Orden.objects.none(),instance=cliente)
        #form = ordenar(initial={'cliente':cliente})
    else:
        try:
            if request.method =='POST' and request.POST['Anadir'] :

                extra+=1
                ordenarSet = inlineformset_factory(Cliente, Orden, fields=('producto', 'estado', 'nota'), extra=extra)
                cliente = Cliente.objects.get(idc=pk)
                formularioset = ordenarSet(queryset=Orden.objects.none(), instance=cliente)

        except:
            if request.method=='POST':
                # form = ordenar(request.POST)
                cliente = Cliente.objects.get(idc=pk)
                ordenarSet = inlineformset_factory(Cliente, Orden, fields=('producto', 'estado', 'nota'), extra=extra)
                formularioset = ordenarSet(request.POST, instance=cliente)
                if formularioset.is_valid():
                    # print(formularioset.cleaned_data)

                    w = 0
                    listaids = []
                    i = 0
                    listaidfs = []
                    ordenesl = Orden.objects.all()
                    for c in ordenesl:
                        listaidfs.append(c.idf)
                        listaids.append(c.id)
                    while i == 0 and i in listaidfs:
                        i = random.randint(1, 1000)

                    dbt = 0
                    for d in formularioset.cleaned_data:
                        w = random.randint(1, 1000)

                        while w in listaids:
                            w = random.randint(1, 1000)

                        try:
                            cd = d
                            clientes = cd['cliente']
                            productos = cd['producto']
                            idfs = i
                            ido = w

                            cd['id'] = ido
                            cd['idf'] = idfs

                            estados = cd['estado']
                            notas = cd['nota']
                            print(formularioset.cleaned_data)

                            if estados != "None":
                                ord = Orden(idf=idfs, id=ido, cliente_id=clientes.idc, producto_id=productos.id, estado=estados,
                                            nota=notas)
                                ord.save()

                                prds = Inventario1.objects.get(id=productos.id)
                                prds.salidas += 1
                                dbt += prds.precioitbis
                                prds.save()

                        except:
                            pass

            # formularioset.save()

            # Introduce la factura al diario general
            qrs = formularioset.cleaned_data[0]['idf']
            diagd = Orden.objects.filter(idf=qrs)
            clnt = Cliente.objects.get(idc=diagd[0].cliente_id)

            diag = Diario(cliente=clnt, detalle='Factura', debito=dbt * 1.18, credito=0, idf=diagd[0])
            diag.save()

            fct = qrs
            return redirect(f'../../facturacion/{fct}/')
    contexto={'formset':formularioset,'pk':pk}
    return render(request,'cuentas/form_ordenar.html',contexto)

def notacredito(request,fct):
    ordns = fct
    prds = Inventario1.objects.all()
    ordenes = Orden.objects.filter(idf=ordns,estado='Devuelto')
    cliente = Cliente.objects.get(idc=ordenes[0].cliente.idc)
    ords = []
    for i in ordenes:
        if i.producto.descripcion not in ords:
            ords.append(i.producto.descripcion)
    contexto = {'idf': ordns, 'fecha': ordenes[0].fecha, 'orden': ordenes, 'cliente': cliente, 'dics': ''}
    vld = []
    total = 0
    for a in ords:
        vls = prds.get(descripcion=a)
        vlc = ordenes.filter(producto__descripcion=vls.descripcion).count()
        vld.append(
            {'nombre': vls.descripcion, 'idpp': vls.id, 'idp': vls.idp.nombre, 'cant': vlc, 'precio': vls.precioitbis,
             'total': vls.precioitbis * vlc})
    for b in vld:
        total += b['total']
    contexto = {'idf': ordns, 'fecha': ordenes[0].fecha, 'orden': ordenes, 'cliente': cliente, 'dics': vld,
                'total': total, 'totali': total * 0.18, 'totalit': total * 1.18}
    return render(request, 'cuentas/notadecredito.html', contexto)
def devolverOrden(request, pk):
    form= devolucionform(pk)

    contexto={'form':form,'pk':pk}
    if request.method =='POST':
        lipr=request.POST['producto']
        ordns=Orden.objects.all()
        if lipr is list:
            fct=ordns.get(id=lipr[0])
        else:
            fct = ordns.get(id=lipr)
        mstr=fct
        clnt=Cliente.objects.get(idc=fct.cliente_id)
        fct= fct.idf
        crd=0

        if lipr is list:
            for i in lipr:

                ord= ordns.get(id=i)
                ord.estado='Devuelto'
                ord.save()

                prds = Inventario1.objects.get(id=ord.producto.id)

                crd += prds.precioitbis
        else:
            ord = ordns.get(id=lipr)
            ord.estado = 'Devuelto'
            ord.save()

            prds = Inventario1.objects.get(id=ord.producto.id)

            crd += prds.precioitbis
        diario=Diario.objects.all()
        try:

            df=diario.get(idf=mstr, detalle='Devolucion')
            df.credito+=crd
            df.save()
        except:
            diag = Diario(cliente=clnt, detalle='Devolucion', debito=0, credito=crd, idf=mstr)
            diag.save()
        return redirect(f'../../notacredito/{fct}/')
    return render(request,'cuentas/form_devolver.html',contexto)
def generar_pdf(template_src,context_dict={}):
    template = get_template(template_src)
    html =template.render(context_dict)
    result = BytesIO()
    pdf=pisa.pisaDocument(BytesIO(html.encode('ISO-8859-1')),result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')


    return None

class DownloadPDF(View):
    def get(self, request,pk, *args, **kwargs):
        ordns = pk
        prds = Inventario1.objects.all()
        ordenes = Orden.objects.filter(idf=ordns)
        cliente = Cliente.objects.get(idc=ordenes[0].cliente.idc)
        ords = []
        for i in ordenes:
            if i.producto.descripcion not in ords:
                ords.append(i.producto.descripcion)
        contexto = {'idf': ordns, 'fecha': ordenes[0].fecha, 'orden': ordenes, 'cliente': cliente, 'dics': ''}
        vld = []
        total = 0
        for a in ords:
            vls = prds.get(descripcion=a)
            vlc = ordenes.filter(producto__descripcion=vls.descripcion).count()
            vld.append({'nombre': vls.descripcion, 'idpp': vls.id, 'idp': vls.idp.nombre, 'cant': vlc,
                        'precio': vls.precioitbis, 'total': vls.precioitbis * vlc})
        for b in vld:
            total += b['total']
        contexto = {'idf': ordns, 'fecha': ordenes[0].fecha, 'orden': ordenes, 'cliente': cliente, 'dics': vld,
                    'total': total, 'totali': total * 0.18, 'totalit': total * 1.18}
        pdf = generar_pdf('cuentas/plantillapdf.html',contexto)

        response = HttpResponse(pdf,content_type='applicaction/pdf')
        filename = "Factura_%s.pdf" %(pk)
        content ="attachment; filename='%s'"%(filename)
        response['Content-Disposition']=content
        return response
class DownloadPDFN(View):
    def get(self, request,pk, *args, **kwargs):
        ordns = pk
        prds = Inventario1.objects.all()
        ordenes = Orden.objects.filter(idf=ordns, estado='Devuelto')
        cliente = Cliente.objects.get(idc=ordenes[0].cliente.idc)
        ords = []
        for i in ordenes:
            if i.producto.descripcion not in ords:
                ords.append(i.producto.descripcion)
        contexto = {'idf': ordns, 'fecha': ordenes[0].fecha, 'orden': ordenes, 'cliente': cliente, 'dics': ''}
        vld = []
        total = 0
        for a in ords:
            vls = prds.get(descripcion=a)
            vlc = ordenes.filter(producto__descripcion=vls.descripcion).count()
            vld.append(
                {'nombre': vls.descripcion, 'idpp': vls.id, 'idp': vls.idp.nombre, 'cant': vlc,
                 'precio': vls.precioitbis,
                 'total': vls.precioitbis * vlc})
        for b in vld:
            total += b['total']
        contexto = {'idf': ordns, 'fecha': ordenes[0].fecha, 'orden': ordenes, 'cliente': cliente, 'dics': vld,
                    'total': total, 'totali': total * 0.18, 'totalit': total * 1.18}
        pdf = generar_pdf('cuentas/plantillapdfN.html',contexto)

        response = HttpResponse(pdf,content_type='applicaction/pdf')
        filename = "Factura_%s.pdf" %(pk)
        content ="attachment; filename='%s'"%(filename)
        response['Content-Disposition']=content
        return response

class ViewPDF(View):
	def get(self, request,pk, *args, **kwargs):


            ordns = pk

            prds = Inventario1.objects.all()
            ordenes = Orden.objects.filter(idf=ordns)
            cliente = Cliente.objects.get(idc=ordenes[0].cliente.idc)
            ords = []
            for i in ordenes:
                if i.producto.descripcion not in ords:
                    ords.append(i.producto.descripcion)
            contexto = {'idf': ordns, 'fecha': ordenes[0].fecha, 'orden': ordenes, 'cliente': cliente, 'dics': ''}
            vld = []
            total = 0
            for a in ords:
                vls = prds.get(descripcion=a)
                vlc = ordenes.filter(producto__descripcion=vls.descripcion).count()
                vld.append({'nombre': vls.descripcion, 'idpp': vls.id, 'idp': vls.idp.nombre, 'cant': vlc,
                            'precio': vls.precioitbis, 'total': vls.precioitbis * vlc})
            for b in vld:
                total += b['total']
            contexto = {'idf': ordns, 'fecha': ordenes[0].fecha, 'orden': ordenes, 'cliente': cliente, 'dics': vld,
                        'total': total, 'totali': total * 0.18, 'totalit': total * 1.18}


            pdf = generar_pdf('cuentas/plantillapdf.html', contexto)
            return HttpResponse(pdf, content_type='application/pdf')

class ViewPDFN(View):
	def get(self, request,pk, *args, **kwargs):
            ordns = pk
            prds = Inventario1.objects.all()
            ordenes = Orden.objects.filter(idf=ordns, estado='Devuelto')
            cliente = Cliente.objects.get(idc=ordenes[0].cliente.idc)
            ords = []
            for i in ordenes:
                if i.producto.descripcion not in ords:
                    ords.append(i.producto.descripcion)
            contexto = {'idf': ordns, 'fecha': ordenes[0].fecha, 'orden': ordenes, 'cliente': cliente, 'dics': ''}
            vld = []
            total = 0
            for a in ords:
                vls = prds.get(descripcion=a)
                vlc = ordenes.filter(producto__descripcion=vls.descripcion).count()
                vld.append(
                    {'nombre': vls.descripcion, 'idpp': vls.id, 'idp': vls.idp.nombre, 'cant': vlc,
                     'precio': vls.precioitbis,
                     'total': vls.precioitbis * vlc})
            for b in vld:
                total += b['total']
            contexto = {'idf': ordns, 'fecha': ordenes[0].fecha, 'orden': ordenes, 'cliente': cliente, 'dics': vld,
                        'total': total, 'totali': total * 0.18, 'totalit': total * 1.18}


            pdf = generar_pdf('cuentas/plantillapdfN.html', contexto)
            return HttpResponse(pdf, content_type='application/pdf')
def modOrden(request, pk):

    orden= Orden.objects.get(id=pk)
    form= ordenar(instance=orden)
    if request.method =='POST':
        form = ordenar(request.POST, instance=orden)
        if form.is_valid():
            form.save()
            return redirect('/')
    contexto={'form':form}
    return render(request, 'cuentas/form_ordenar2.html', contexto)


def borrarOrden(request, pk):



    orden = Orden.objects.get(id=pk)
    prd=Inventario1.objects.get(id=orden.producto_id)
    diario = Diario.objects.get(cliente_id=orden.cliente_id)
    if request.method=='POST':
        prd.salidas-=1
        prd.save()
        print(diario.debito)
        diario.debito=diario.debito - orden.producto.precioitbis

        print(diario.debito)

        orden.delete()
        diario.save()
        return redirect('/')
    context = {'item': orden}
    return render(request, 'cuentas/delete.html', context)
