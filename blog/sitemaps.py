from django.contrib.sitemaps import Sitemap
from .models import Hojavida


class HojavidaSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Hojavida.objects.filter(status=1)

    def lastmod(self, obj):
        return obj.updated_on

    # def location(self, item):
    #     return reverse(item)
