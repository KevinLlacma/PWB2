from django.db import models
from .customer import Customer

class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10,decimal_places=2)

    status = models.BooleanField(default=True, null=False)
    created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)

    # class Meta:
    #     managed = True
    #     db_table = 'categorias'
    def __str__(self):
        return "%s %s" % (self.customer,self.date)
