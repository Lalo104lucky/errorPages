from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from datetime import datetime

class StaticViewSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0

    def items(self):
        return ['index']

    def location(self, item):
        return reverse(item)

    def lastmod(self, item):
        # Retorna la fecha de última modificación (puedes usar un campo dinámico)
        return datetime.now()  # Aquí es estático, pero puedes obtenerlo dinámicamente