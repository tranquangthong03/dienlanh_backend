from rest_framework import viewsets
from .models import Category, Product
from .serializers import CategorySerializers, ProductSerializers

#ModelViewSet để tự sinh các API CRUD
class CategoryViewSet(viewsets.ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializers

class ProductViewSet(viewsets.ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializers

