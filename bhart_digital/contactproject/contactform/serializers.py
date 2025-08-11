# contactform/serializers.py

from rest_framework import serializers
from .models import ContactFormSubmission
from .models import Blogs

class ContactFormSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactFormSubmission
        fields = ['contact_id', 'name', 'email', 'phone', 'message', 'submitted_at']
        read_only_fields = ['contact_id', 'submitted_at']


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = '__all__'

        extra_kwargs = {
                'created_at': {'format': '%B %d, %Y'}
            }