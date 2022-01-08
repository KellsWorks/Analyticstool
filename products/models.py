from django.db import models


class Product(models.Model):
    owner = models.ForeignKey('authapp.User', null=True, related_name='products', on_delete=models.CASCADE)
    name = models.CharField('name', max_length=100)
    description = models.TextField('Description')
    amount = models.IntegerField('amount')
    cost = models.IntegerField('cost')
    price = models.IntegerField('price')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
