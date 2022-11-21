from rest_framework import serializers

from npo_project.models import FAQ


class FAQSerializer(serializers.ModelSerializer):

    class Meta:
        model = FAQ
        fields = ['question', 'answer']