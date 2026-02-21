from django.urls import path
from . import views


urlpatterns =[
    path('',views.inicio,name='inicio'),
path('login/',views.login,name='login'),
    path('registro/',views.registro,name='registro'),
    path('productos/',views.productos,name='productos'),
    path('proveedores/',views.proveedores,name='proveedores'),
    path('crearCliente/',views.crearCliente, name='crear_cliente'),
    path('modCliente/<str:pk>/', views.modCliente, name='modificar_cliente'),
    path('facturas/<str:pk>/',views.facturas, name='facturas_clientes'),
    path('empleados/',views.empleados,name='empleados'),
    path('clientes/',views.mclientes, name='clientes'),
    path('impresion/<str:pk>/',views.ViewPDF.as_view(), name='PDF'),
path('impresiondesc/<str:pk>/',views.DownloadPDF.as_view(), name='PDFD'),
path('impresionN/<str:pk>/',views.ViewPDFN.as_view(), name='PDFN'),
path('impresionNdesc/<str:pk>/',views.DownloadPDFN.as_view(), name='PDFDN'),
    path('cliente/<str:pk_test>/',views.cliente,name='cliente'),
    path('crearorden/<str:pk>/',views.crearOrden, name='crear_orden'),
    path('devolverorden/<str:pk>/', views.devolverOrden, name='devolver_orden'),

    path('modorden/<str:pk>/',views.modOrden, name='mod_orden'),
    path('borrarorden/<str:pk>/',views.borrarOrden, name='borrar_orden'),
path('crearprod/',views.crearProd, name='crear_prod'),
    path('modprod/<str:pk>/',views.modProd, name='mod_prod'),
    path('borrarprod/<str:pk>/',views.borrarProd, name='borrar_prod'),
path('crearprov/',views.crearProv, name='crear_prov'),
    path('modprov/<str:pk>/',views.modProv, name='mod_prov'),
    path('borrarprov/<str:pk>/',views.borrarProv, name='borrar_prov'),
path('crearempl/',views.crearEmpl, name='crear_empl'),
    path('modempl/<str:pk>/',views.modEmpl, name='mod_empl'),
    path('borrarempl/<str:pk>/',views.borrarEmpl, name='borrar_empl'),
path('borrarcliente/<str:pk>/',views.borrarCliente, name='borrar_cliente'),
path('ordenes/',views.ordenes, name='ordenes'),
    path('login/',views.login),
path('cerrar/',views.cerrar),
    path('facturacion/<str:fct>/',views.factura, name='factura'),
    path('notacredito/<str:fct>/', views.notacredito, name='notacredito')

]