from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Blogs  # Import your Blog model

# For dynamic blog posts
# Sitemap for dynamic blog posts
class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Blogs.objects.all().order_by("blog_id")

    def location(self, obj):
        return reverse("blog_detail", args=[obj.blog_id])

    def lastmod(self, obj):
        return obj.created_at   # assumes Blogs model has created_at field


# For static pages
class StaticViewSitemap(Sitemap):
    priority = 0.6   # Importance of these pages
    changefreq = "daily"  # How often search engines should re-crawl

    def items(self):
        # Return all static view names (the same names you used in urls.py)
        return [
            "home",
            "about",
            "digital_marketing",
            "game_development",
            "mobile_development",
            "services",
            "web_development",
            "contact",
            "blog",
            "web_security",
            "business_consultant",
            "ai_ml",
            "ui-ux-design",
            "chatbot_development",
        ]

    def location(self, item):
        # Convert the name into an actual URL
        return reverse(item)
