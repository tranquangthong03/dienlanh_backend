from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Tên danh mục")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    name = models.CharField(max_length=200, verbose_name="Tên sản phẩm")
    description = models.TextField(verbose_name="Mô tả chi tiết")
    price = models.DecimalField(max_digits=12, decimal_places=0, verbose_name="Giá bán (VND)")
    stock = models.PositiveIntegerField(default=0, verbose_name="Số lượng tồn kho")
    
    # Cần pip install Pillow nếu chưa cài
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="Hình ảnh")

    def __str__(self):
        return self.name