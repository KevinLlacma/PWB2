from django.db import models
from .product import Product
from .category import Category
class ProductCategory(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    status = models.BooleanField(default=True, null=False)
    created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)

    # class Meta:
    #     managed = True
    #     db_table = 'categorias'
    def __str__(self):
        return "%s %s" % (self.product, self.category)
