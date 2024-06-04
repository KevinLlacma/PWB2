from django.db import models
from django.utils.translation import gettext_lazy as _

from .order import Order
from .product import Product

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE) 
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10,decimal_places=2)
    subtotal = models.DecimalField(max_digits=10,decimal_places=2)
    
     

    status = models.BooleanField(default=True, null=False)
    created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)

    # class Meta:
    #     managed = True
    #     db_table = 'categorias'
    def __str__(self):
        return "%s %s %s" % (self.order, self.product, self.quantity)
