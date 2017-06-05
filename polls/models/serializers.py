from rest_framework import serializers
from polls.models.models import Customer,Product

class CustomerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(required=True, allow_blank=False,max_length=100)
    last_name = serializers.CharField(required=True, allow_blank=False, max_length=100)

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, allow_blank=False,max_length=100)
    price = serializers.IntegerField(required=True, allow_blank=False)

