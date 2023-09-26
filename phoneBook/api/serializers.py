from rest_framework import serializers
from ..models import Category, Phone


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
        
class PhoneSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)
    
    class Meta:
        model = Phone
        fields = '__all__'