from django.db import connection

class MultiTenantMiddleware:
    """Middleware to handle multi-tenancy based on subdomains."""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tenant = self.get_tenant(request)
        with connection.cursor() as cursor:
            # Set the schema for this request
            cursor.execute(f"SET search_path TO {tenant}, public;")
        
        response = self.get_response(request)
        
        return response

    def get_tenant(self, request):
        """Extracts the tenant name from the subdomain."""
        host = request.get_host()
        parts = host.split('.')
        # Check for subdomains like tenant1.localhost
        if len(parts) > 2 and parts[0] != 'www' and parts[1] == 'localhost':
            return parts[0]
        return 'public'

