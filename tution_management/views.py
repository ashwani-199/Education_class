from django.http import HttpResponse
from django.views.decorators.http import require_GET

@require_GET
def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow: /admin/",
        "Allow: /",
        f"Sitemap: https://{request.get_host()}/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")


@require_GET
def ads_txt(request):
    # Replace with your actual publisher ID from AdSense
    content = "google.com, pub-1678059963139758, DIRECT, f08c47fec0942fa0"
    return HttpResponse(content, content_type="text/plain")