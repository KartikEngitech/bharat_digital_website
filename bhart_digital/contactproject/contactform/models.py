from django.db import models
from django.urls import reverse

# Create your models here.

class ContactFormSubmission(models.Model):
    contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True, default="")
    email = models.EmailField(null=True, blank=True, default="")
    phone = models.CharField(max_length=20, null=True, blank=True, default="")
    message = models.TextField(null=True, blank=True, default="")
    submitted_at = models.DateTimeField(auto_now_add=True)  # ✅ fixed line



class Blogs(models.Model):
    blog_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Example: /blog/slug/
        return reverse("blog_detail", kwargs={"blog_id": self.blog_id})



