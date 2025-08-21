
# Create your views here.

from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .serializers import ContactFormSubmissionSerializer, BlogSerializer
from .models import ContactFormSubmission, Blogs
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.urls import reverse

@swagger_auto_schema(
    method='post',
    operation_summary="Submit Contact Form",
    request_body=ContactFormSubmissionSerializer,
    responses={200: "Success", 400: "Validation Error"}
)

@api_view(['POST'])
@permission_classes([AllowAny])
def contact_add(request):
    serializer = ContactFormSubmissionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        # Extract fields from validated data
        name = serializer.validated_data.get('name')
        email = serializer.validated_data.get('email')
        message = serializer.validated_data.get('message')  # Assuming a 'message' field exists
        phone = serializer.validated_data.get('phone')  # Assuming a 'message' field exists

        # # Email to user (confirmation)
        # send_mail(
        #     subject="Thank you for contacting us!",
        #     message=f"Hi {name},\n\nThank you for reaching out. We have received your message:\n\n\"{message}\"\n\nWe will get back to you soon.",
        #     from_email=settings.DEFAULT_FROM_EMAIL,
        #     recipient_list=[email],
        #     fail_silently=False,
        # )

        # # Email to admin/support
        # send_mail(
        #     subject="New Contact Form Submission",
        #     message=f"New submission received:\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nRequirement: {message}",
        #     from_email=settings.DEFAULT_FROM_EMAIL,
        #     recipient_list=[settings.CONTACT_NOTIFICATION_EMAIL],  # Define this in settings.py
        #     fail_silently=False,
        # )

        return Response({'success': "1", 'message': 'Form submitted successfully'})
    
    return Response({'success': "0", 'errors': serializer.errors}, status=400)





# @api_view(['POST'])
# @permission_classes([AllowAny])
# def contact_view(request):
#     serializer = ContactFormSubmissionSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({'success': "1", 'message': 'Form submitted successfully'})
#     return Response({'success': "0", 'errors': serializer.errors}, status=400)


@api_view(['GET'])
@permission_classes([AllowAny])
def contact_list(request):
    contacts = ContactFormSubmission.objects.all()
    serializer = ContactFormSubmissionSerializer(contacts, many=True)
    return Response({'success': "1",'message': 'Contact data retrieved successfully', 'data': serializer.data})


@swagger_auto_schema(
    method='put',
    operation_summary="Update Contact Form",
    request_body=ContactFormSubmissionSerializer,
    responses={200: "Success", 400: "Validation Error"}
)
@api_view(['PUT'])
@permission_classes([AllowAny])
def contact_update(request, contact_id):
    try:
        contact = ContactFormSubmission.objects.get(pk=contact_id)
    except ContactFormSubmission.DoesNotExist:
        return Response({'success': "0", 'message': "Contact not found"}, status=404)

    serializer = ContactFormSubmissionSerializer(contact, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'success': "1", 'message': "Contact updated successfully"})
    return Response({'success': "0", 'errors': serializer.errors}, status=400)


@api_view(['DELETE'])
@permission_classes([AllowAny])
def contact_delete(request, contact_id):
    try:
        contact = ContactFormSubmission.objects.get(pk=contact_id)
    except ContactFormSubmission.DoesNotExist:
        return Response({'success': "0", 'message': "Contact not found"}, status=404)

    contact.delete()
    return Response({'success': "1", 'message': "Contact deleted successfully"})



@swagger_auto_schema(method='post', request_body=BlogSerializer)
@api_view(['POST'])
@permission_classes([AllowAny])
def add_blog(request):
    serializer = BlogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'success': "1", 'message': 'Blog added successfully'})
    return Response({'success': "0", 'errors': serializer.errors}, status=400)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_blogs(request):
    blogs = Blogs.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response({'success': "1",'message': 'Blog data retrieved successfully', 'blogs': serializer.data})

@swagger_auto_schema(method='put', request_body=BlogSerializer)
@api_view(['PUT'])
@permission_classes([AllowAny])
def update_blog(request, blog_id):
    try:
        blog = Blogs.objects.get(pk=blog_id)
    except Blogs.DoesNotExist:
        return Response({'success': "0", 'message': 'Blog not found'}, status=404)

    serializer = BlogSerializer(blog, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'success': "1", 'message': 'Blog updated successfully'})
    return Response({'success': "0", 'errors': serializer.errors}, status=400)

@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_blog(request, blog_id):
    try:
        blog = Blogs.objects.get(pk=blog_id)
        blog.delete()
        return Response({'success': "1", 'message': 'Blog deleted successfully'})
    except Blogs.DoesNotExist:
        return Response({'success': "0", 'message': 'Blog not found'}, status=404)



# Home
@swagger_auto_schema(method='get', operation_summary="Render Home Page")
@api_view(['GET'])
def home_view(request):
    return render(request, 'index.html')

# About
@swagger_auto_schema(method='get', operation_summary="Render About Page")
@api_view(['GET'])
def about_view(request):
    return render(request, 'about.html')

# Digital Marketing
@swagger_auto_schema(method='get', operation_summary="Render Digital Marketing Page")
@api_view(['GET'])
def digital_marketing_view(request):
    return render(request, 'DigitalMarketing.html')

# Game Development
@swagger_auto_schema(method='get', operation_summary="Render Game Development Page")
@api_view(['GET'])
def game_development_view(request):
    return render(request, 'GameDevelopment.html')

# Mobile Development
@swagger_auto_schema(method='get', operation_summary="Render Mobile Development Page")
@api_view(['GET'])
def mobile_development_view(request):
    return render(request, 'Mobile Development.html')

# Service
@swagger_auto_schema(method='get', operation_summary="Render Service Page")
@api_view(['GET'])
def service_view(request):
    return render(request, 'service.html')

# Web Development
@swagger_auto_schema(method='get', operation_summary="Render Web Development Page")
@api_view(['GET'])
def web_development_view(request):
    return render(request, 'Web Development.html')


# Contact
@swagger_auto_schema(method='get', operation_summary="Render Contact Page")
@api_view(['GET'])
def contacts_view(request):
    return render(request, 'contact.html')

# Blog
@swagger_auto_schema(method='get', operation_summary="Render Blog Page")
@api_view(['GET'])
def blog_view(request):
    return render(request, 'blog.html')

# Web Security
@swagger_auto_schema(method='get', operation_summary="Render Web Security Page")
@api_view(['GET'])
def web_security_view(request):
    return render(request, 'WebSecurity.html')

# Chatbot
@swagger_auto_schema(method='get', operation_summary="Render Chatbot Page")
@api_view(['GET'])
def chatbot_view(request):
    return render(request, 'chatbot.html')

# UI/UX
@swagger_auto_schema(method='get', operation_summary="Render Ui/Ux Page")
@api_view(['GET'])
def ui_ux_view(request):
    return render(request, 'ui-ux.html')

# AI/ML
@swagger_auto_schema(method='get', operation_summary="Render AI/ML Page")
@api_view(['GET'])
def ai_ml_view(request):
    return render(request, 'ai-ml.html')

# Business
@swagger_auto_schema(method='get', operation_summary="Render Businees Page")
@api_view(['GET'])
def business_view(request):
    return render(request, 'Business.html')





def robots_txt(request):
    # Build absolute URL for the sitemap index
    sitemap_url = request.build_absolute_uri(reverse("sitemap-index"))
    content = f"User-agent: *\nAllow: /\nSitemap: {sitemap_url}\n"
    return HttpResponse(content, content_type="text/plain")


# Blog detail view
def blog_detail(request, blog_id):
    """
    Fetch a single blog post by its ID and render it.
    """
    blog = get_object_or_404(Blog, blog_id=blog_id)
    return render(request, "blog_detail.html", {"blog": blog})
