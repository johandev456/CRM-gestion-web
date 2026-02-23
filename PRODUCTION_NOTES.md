# Configuration for production
# Run collectstatic before deploying:
# python manage.py collectstatic --noinput

# This file should be checked in version control
# Update these values before deploying to production

# Set DEBUG=False for production
DEBUG = False

# List your domain names here
ALLOWED_HOSTS = ['*']  # Change to specific domains in production

# Database should use dj-database-url to get connection from environment variable
# Example: DATABASE_URL=postgresql://user:password@host:port/dbname

# Static files will be served by WhiteNoise middleware
# No need for separate static file server

# Security Headers (uncomment when using HTTPS)
# SECURE_SSL_REDIRECT = True
# SECURE_HSTS_SECONDS = 31536000
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
