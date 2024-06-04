from django.contrib import admin

from .models.category import Category
from .models.customer import Customer
from .models.order_detail import OrderDetail
from .models.order import Order
from .models.product import Product
from .models.product_category import ProductCategory


# Register your models here.
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(OrderDetail)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(ProductCategory)
