from rest_framework import serializers
from .models import Category, Product

class CategorySerializers(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = '__all__'

class ProductSerializers(serializers.ModelSerializer):
  # Lấy thêm thông tin category thay vì chỉ lấy ID
  category_name = serializers.ReadOnlyField(source='category.name')
  class Meta:
    model = Product
    fields = '__all__'