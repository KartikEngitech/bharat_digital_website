from django.urls import path
from .views import contact_add, contact_list, contact_update, contact_delete
from .views import add_blog, get_blogs, update_blog, delete_blog
from .views import home_view, about_view, digital_marketing_view, game_development_view
from .views import mobile_development_view, service_view, web_development_view
from .views import contacts_view, blog_view, web_security_view, chatbot_view
from .views import ui_ux_view, ai_ml_view, business_view
from .models import Blogs
from .views import robots_txt   # we’ll add this in views.py
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import Sitemap
from . import views

class BlogSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Blogs.objects.all()

    def lastmod(self, obj):
        return obj.created_at   # using created_at from your Blogs model

sitemaps = {
    "blogs": BlogSitemap,
}


urlpatterns = [
    # Contact form URLs
    path('contact_add/', contact_add, name='contact_add'),
    path('contact_list/', contact_list, name='contact_list'),
    path('contact_update/<int:contact_id>/', contact_update, name='contact_update'),
    path('contact_delete/<int:contact_id>/', contact_delete, name='contact_delete'),

    # Blog URLs
    path('add_blog/', add_blog, name='add_blog'),
    path('get_blogs/', get_blogs, name='get_blogs'),
    path('update_blog/<int:blog_id>/', update_blog, name='update_blog'),
    path('delete_blog/<int:blog_id>/', delete_blog, name='delete_blog'),

    path('', home_view, name='home_view'),
    path('about_view/', about_view, name='about_view'),
    path('digital_marketing_view/', digital_marketing_view, name='digital_marketing_view'),
    path('game_development_view/', game_development_view, name='game_development_view'),
    path('mobile_development_view/', mobile_development_view, name='mobile_development_view'),
    path('service_view/', service_view, name='service_view'),
    path('web_development_view/', web_development_view, name='web_development_view'),
    path('contacts_view/', contacts_view, name='contacts_view'),
    path('blog_view/', blog_view, name='blog_view'),
    path('web_security_view/', web_security_view, name='web_security_view'),
    path('business_view/', business_view, name='business_view'),
    path('ai_ml_view/', ai_ml_view, name='ai_ml_view'),
    path('ui_ux_view/', ui_ux_view, name='ui_ux_view'),
    path('chatbot_view/', chatbot_view, name='chatbot_view'),


    # ✅ Blog detail (matches model reverse and sitemap)
    path("blog/<int:blog_id>/", views.blog_detail, name="blog_detail"),

    # robots.txt (optional but recommended)
    path("robots.txt", views.robots_txt, name="robots_txt"),

]