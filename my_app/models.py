from django.db import models


class ProductsModel(models.Model):
    product_name = models.CharField(max_length=30)
    cost = models.CharField(max_length=6)

    def __unicode__(self):
        dict = {}
        dict['product_name'] = self.product_name
        dict['cost'] = self.cost
        return dict