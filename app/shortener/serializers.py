from rest_framework import serializers


class UrlSerializer(serializers.Serializer):
    original_url = serializers.CharField()
    short_url = serializers.CharField()