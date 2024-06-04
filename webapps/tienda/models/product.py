from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)

    status = models.BooleanField(default=True, null=False)
    created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)

    # class Meta:
    #     managed = True
    #     db_table = 'categorias'
    def __str__(self):
        return "%s %" % (self.name, self.stock)
