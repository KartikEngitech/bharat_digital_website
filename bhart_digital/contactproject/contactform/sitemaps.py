from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Blogs  # Import your Blog model

# For dynamic blog posts
class BlogSitemap(Sitemap):
    changefreq = "weekly"   # How often search engines should check
    priority = 0.8          # Priority (0.0 - 1.0)

    def items(self):
        return Blogs.objects.all().order_by('blog_id')

    def location(self, obj):
        return f"https://bharatdigital.co{reverse('blog_detail', args=[obj.blog_id])}"


# For static pages
class StaticViewSitemap(Sitemap):
    priority = 0.8   # Importance of these pages
    changefreq = "daily"  # How often search engines should re-crawl

    def items(self):
        # Return all static view names (the same names you used in urls.py)
        return [
            "home_view",
            "about_view",
            "digital_marketing_view",
            "game_development_view",
            "mobile_development_view",
            "service_view",
            "web_development_view",
            "contacts_view",
            "blog_view",
            "web_security_view",
            "business_view",
            "ai_ml_view",
            "ui_ux_view",
            "chatbot_view",
        ]

    def location(self, item):
        # Convert the name into an actual URL
        return f"https://bharatdigital.co{reverse(item)}"
