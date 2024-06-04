from django.db import models


class Customer(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100);
    direction = models.CharField(max_length=100)

    status = models.BooleanField(default=True, null=False)
    created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    modified = models.DateTimeField(null=False, auto_now=True)

    # class Meta:
    #     managed = True
    #     db_table = 'categorias'
    def __str__(self):
        return "%s" % (self.name)
