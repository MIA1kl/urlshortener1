from rest_framework import serializers
from .models import UrlData


class UrlDataSerializer(serializers.ModelSerializer):
    model = UrlData
    fields = ('url', 'shorturl')
