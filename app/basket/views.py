from django.shortcuts import render
from django.urls import reverse
from catalog.models import * 
# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from catalog.models import *
from .basket import *
from .forms import BasketAddProductForm
import pprint
from django.http import JsonResponse

def BasketAdd(request): 
	basket = Basket(request)
	cd = request.GET
	discount = 0 
	obj = SaleProduct.objects.get(id=cd["product"])
	price = obj.price
	discount = 0
	basket.add(product=cd["product"], quantity=cd['quantity'],price=price,discount=discount)
	# z = round(basket.total_basket, 2)
	return JsonResponse({'quantity':basket.basket_count}, safe=False)

def BasketRemove(request, product_id):
	basket = Basket(request)
	product = product_id
	basket.remove(product)
	return redirect('/basket')

def BasketDetail(request):
	category = Category.objects.all()
	basket = Basket(request)
	# basket.clear()
	# pprint.pprint(len(basket))
	# for i in basket:
	# 	pprint.pprint(i)
	return render(request, 'basket/cart.html',locals())