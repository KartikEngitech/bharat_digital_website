from django.contrib import admin

# Register your models here.
from .models import ContactFormSubmission, Blogs

admin.site.register(ContactFormSubmission)
admin.site.register(Blogs)