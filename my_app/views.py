from django.shortcuts import render
from django.views import View
from my_app.models import ProductsModel


class ProductView(View):
    def get(self, request):
        # product = ProductsModel(product_name="Хлеб", cost="25")
        # product.save()
        products = ProductsModel.objects.all()
        data = {
            'products': products
        }

        return render(request, 'products.html', data)
