# LibraryProject/middleware.py
class ContentSecurityPolicyMiddleware:
    """
    Simple CSP header middleware (fallback).
    Adjust the directive values to reflect your real static & CDN domains.
    """
    def _init_(self, get_response):
        self.get_response = get_response
        self.csp = (
            "default-src 'self'; "
            "script-src 'self' 'unsafe-inline'; "
            "style-src 'self' 'unsafe-inline'; "
            "img-src 'self' data:; "
            "font-src 'self' data:; "
            "object-src 'none'; "
            "frame-ancestors 'none';"
        )

    def _call_(self, request):
        response = self.get_response(request)
        # Don't overwrite if some other middleware set it
        if "Content-Security-Policy" not in response:
            response["Content-Security-Policy"] = self.csp
        return response