from django.contrib import sitemaps
from django.urls import reverse
from apps.blog.models import Post
from django.contrib.sitemaps import Sitemap

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        # Add the 'name' of your URLs here
        return ['home', 'contact', 'about', 'privacy', 'terms']

    def location(self, item):
        return reverse(item)


class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Post.objects.filter(status=1)

    def lastmod(self, obj):
        return obj.updated_on