from django.shortcuts import render
from catalog.models import *
# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login as dj_login
from django.urls import reverse
from .forms import *
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, get_object_or_404 ,render_to_response
from django.http import HttpResponse
from django.template import loader, RequestContext
import pprint
from .models import *
from django.views.decorators.http import require_POST
from django.template.loader import render_to_string
from django.conf import settings
from lk.models import User as Userr

from django.core.mail import send_mail
from datetime import date, datetime
from django.contrib.auth import logout
from order.models import *



def send_email_order_manager(a,b,c):
	subject = 'Заказ обратного звонка на Vsempostel.ru'
	h = 'lurc89@mail.ru'
	html_message = render_to_string('mail/callback.html',{'name':a,'phone':b,'questions':c})
	message = ""
	send_mail(subject,message,settings.EMAIL_HOST_USER,[h],html_message=html_message)

@login_required(login_url='/login')
def lk(request):
	# product = Product.objects.get(id=1)
	# pprint.pprint(product.torg)
	category = Category.objects.all()


	return render(request,'lk/cabinet1.html', locals())
@login_required(login_url='/login')
def orders(request):
	orders = Order.objects.filter(new_name=request.user)
	# product = Product.objects.get(id=1)
	# pprint.pprint(product.torg)
	category = Category.objects.all()


	return render(request,'lk/cabinet2.html', locals())
@login_required(login_url='/login')
def cabinet3(request,id):
	order = Order.objects.get(id=id)
	items = OrderItem.objects.filter(order=order)
	delivery = Delivery.objects.filter(order=order)
	oplata = Oplata.objects.filter(order=order)
	# product = Product.objects.get(id=1)
	# pprint.pprint(product.torg)
	category = Category.objects.all()


	return render(request,'lk/cabinet3.html', locals())
@login_required(login_url='/login')
def cabinet4(request):
	# product = Product.objects.get(id=1)
	# pprint.pprint(product.torg)
	category = Category.objects.all()


	return render(request,'lk/cabinet4.html', locals())
@login_required(login_url='/login')
def cabinet5(request):
	# product = Product.objects.get(id=1)
	# pprint.pprint(product.torg)


	category = Category.objects.all()
	return render(request,'lk/cabinet5.html', locals())
@login_required(login_url='/login')
def profile(request):
	usern = Userr.objects.get(username=request.user.username)
	pprint.pprint(usern)
	category = Category.objects.all()


	return render(request,'lk/cabinet6.html', locals())
@login_required(login_url='/login')
def history(request):
	orders = Order.objects.filter(new_name=request.user)
	# product = Product.objects.get(id=1)
	# pprint.pprint(product.torg)

	category = Category.objects.all()

	return render(request,'lk/cabinet2.html', locals())

# def login(request):
# 	# product = Product.objects.get(id=1)
# 	# pprint.pprint(product.torg)
# 	category = Category.objects.all()


# 	return render(request,'lk/login.html', locals())

def password(request):
	# product = Product.objects.get(id=1)
	# pprint.pprint(product.torg)
	category = Category.objects.all()


	return render(request,'lk/password.html', locals())

def password2(request):
	# product = Product.objects.get(id=1)
	# pprint.pprint(product.torg)

	category = Category.objects.all()

	return render(request,'lk/password2.html', locals())

def reg(request):
	# product = Product.objects.get(id=1)
	# pprint.pprint(product.torg)

	category = Category.objects.all()
	userform = UserForm(request.POST)

	if request.method == 'POST':
		
		
		if userform.is_valid():
			cd = userform.cleaned_data
			name = cd['first_name']
			login = cd['username']
			password = cd['password']
			numberphone = cd['numberphone']

			var = Userr.objects.create_user(login,'', password)
			var.first_name = name
			var.numberphone=numberphone
			var.email = cd['username']
			# var.groups.set(group)
			var.save()
			dj_login(request, var)
			userform = UserForm()
			return redirect("/")		
	else:

		userform = UserForm()
	return render(request,'lk/reg.html', locals())

def logout1(request):
	logout(request)
	return redirect("/")

def login(request):
	categories = Category.objects.all()
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				dj_login(request, user)
				# Redirect to a success page.
				return redirect("/")
			else:
				# Return a 'disabled account' error message
				return redirect("/login")

			   
		else:
			# Return an 'invalid login' error message.
			return redirect("/")
	return render(request, 'lk/login.html', locals())

def formsubscribe(request):
	if request.method == 'POST':
		form = SubForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = SubForm()
	return redirect('/')

def callback(request):
	if request.method == 'POST':
		form = CallForm(request.POST)
		if form.is_valid():
			z = form.save()
			send_email_order_manager(z.name,z.phone,z.questions)
			return redirect('/')
	else:
		form = CallForm()
	return redirect('/')



