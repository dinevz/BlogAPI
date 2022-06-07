from rest_framework import serializers
from .models import Peanut

class PeanutSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'title', 'body', 'created_at', 'image_url',)
        model = Peanut