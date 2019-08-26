# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from basket.basket import * 
from catalog.models import * 
from lk.models import * 
from .forms import *
import pprint
from django.conf import settings
from yandex_checkout import *
import requests
from django.http import JsonResponse
import json
from lk.models import User
from django.contrib.auth import authenticate, login as dj_login
from django.template.loader import render_to_string
from django.core.mail import send_mail

def make_ya(orderid,paidid):
	order = Order.objects.get(id=orderid)
	paid = Oplata.objects.get(id=paidid)
	desc = "Заказ № " + str(order.id) + " Оплата № " + str(paid.id)
	payment = Payment.create({"amount": {"value": order.total_all,"currency": "RUB"},
		"payment_method_data": {"type": "bank_card"},
		"confirmation": {"type": "redirect",
		"return_url": "http://vsempostel.tlab-nsk.ru/catalog"},
		"capture": 'true',
		"description": desc})
	z = payment.id
	f = payment.confirmation.confirmation_url
	ret = {"url": f,"id_ya":z}
	return ret
# Create your views here.
def order1(request,pk):
	category = Category.objects.all()
	order = Order.objects.get(id=pk)
	oplata = Oplata.objects.get(order=order)

	if oplata.name_new.id == 1:
		ya = make_ya(order.id,oplata.id)
		oplata.payment_id = ya['id_ya']
		url_to_paid = ya['url']
		oplata.price = int(oplata.price)
		oplata.save()
	# product = Product.objects.get(id=1)
	# pprint.pprint(product.torg)



	return render(request,'order/order.html', locals())

def get_money():
	payment = Payment.create({"amount": {"value": 100,"currency": "RUB"},
		"payment_method_data": {"type": "bank_card"},
		"confirmation": {"type": "redirect",
		"return_url": "http://vsempostel.tlab-nsk.ru/catalog"},
		"capture": 'true',
		"description": "Описание"})
	z = payment
	f = payment.confirmation.confirmation_url
	return f

def send_email_autoreg(a):
	subject = 'Регистрация на Vsempostel.ru'
	html_message = render_to_string('mail/autoreg.html',{'login':a,'pass':'172323172323'})
	message = ""
	host = 'lurc89@mail.ru'
	send_mail(subject,message,host,[a],html_message=html_message)

def send_email_order_customer(a,b):
	subject = 'Заказ на Vsempostel.ru'
	host = 'lurc89@mail.ru'
	html_message = render_to_string('mail/order.html',{'zakaz':b})
	message = ""
	send_mail(subject,message,host,[a],html_message=html_message)

def send_email_order_manager(b):
	subject = 'Заказ на Vsempostel.ru'
	host = 'lurc89@mail.ru'
	a = 'lurc89@mail.ru'
	html_message = render_to_string('mail/not_order.html',{'zakaz':b})
	message = ""
	send_mail(subject,message,host,[a],html_message=html_message)

def order(request):
	# z =get_money()

	category = Category.objects.all()
	basket = Basket(request)
	if request.method == 'POST':
		form = OrderForm(request.POST)
		if form.is_valid():
			if request.user.is_anonymous:
				order = form.save()
			else:
				
				order =  form.save(commit=False)
				order.new_name = request.user
				order.save()

			for i in basket:
				items = OrderItem()
				items.order = order
				items.product_name = i['product']
				items.atributeproduct = i['id']
				items.atributeproduct_name = i['name']
				items.price = i['price']
				items.quantity = i['quantity']
				items.save()

			delivery = Delivery()
			delivery.order = order
			delivery.dostavka = order.order_delivery
			delivery.status_new = 'Новый'
			if order.order_delivery.id ==2:

				delivery.price = 250
			else:
				delivery.price = 0
			delivery.save()

			oplata = Oplata()
			oplata.order = order
			# oplata. = 
			oplata.name_new =order.order_payment
			oplata.price = order.total_all
			oplata.status_new = 'NEW'
			oplata.save()




			basket.clear()

			if request.user.is_anonymous:
				login = order.email
				password = "172323172323"

				var = User.objects.create_user(login,'', password)
				var.first_name = order.first_name
				# var.numberphone=new_order.numberphone
				# var.groups.set(group)
				var.save()
				dj_login(request, var)
				order.new_name = var
				order.save()
				send_email_autoreg(order.email)
			# return render(request, 'order/order.html',locals())
			send_email_order_customer(order.email,order.id)
			send_email_order_manager(order.id)
			success = "/"+ str(order.id)+"/success"
			return redirect(success)

	else:
		form = OrderForm()
	return render(request,'order/order1.html', locals())

def order2(request):
	# product = Product.objects.get(id=1)
	# pprint.pprint(product.torg)



	return render(request,'order/order2.html', locals())

def order3(request):
	# product = Product.objects.get(id=1)
	# pprint.pprint(product.torg)



	return render(request,'order/order3.html', locals())

def order4(request):
	# product = Product.objects.get(id=1)
	# pprint.pprint(product.torg)



	return render(request,'order/order4.html', locals())

def order5(request):
	# product = Product.objects.get(id=1)
	# pprint.pprint(product.torg)



	return render(request,'order/order5.html', locals())

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
@csrf_exempt
def check_paiment(request):
	if request.method == 'POST':
		# pprint.pprint(request.body)
		rerr = request.body.decode("utf-8") 
		# pprint.pprint(rerr)
		event_json = json.loads(rerr)
		# pprint.pprint(event_json)

		try:
			notification_object = WebhookNotification(event_json)
		except Exception:
			a = 1
		payment = notification_object.object
		if payment:
			

			objOplata = Oplata.objects.filter(payment_id=payment.id)
			if objOplata:
				for i in objOplata:
					if payment.status == 'succeeded':
						i.paid = True
						i.status_new = 'PAID'
						i.price = int(oplata.price)
						i.save()
					if payment.status == 'canceled':
						i.status_new = 'CANCEL'
						i.price = int(oplata.price)
						# pprint.pprint(i.get_status_new_display())
						i.save()
						# pprint.pprint(i.get_status_new_display())
					if payment.status == 'pending':
						i.status_new = 'NEW'
						i.price = int(oplata.price)
						i.save()


	return HttpResponse(status=200)