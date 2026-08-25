from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet) # Có nghĩa là các path có categories sẽ do CategoryViewSet xử lý
router.register(r'products', ProductViewSet)

urlpatterns = [
  path('', include(router.urls))
]