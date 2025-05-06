from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticSitemap(Sitemap):
    def items(self):
        return ['home', 'contact']
    
    def location(self, item):
        return reverse(item)