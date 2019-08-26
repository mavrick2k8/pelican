from django.shortcuts import render,redirect
from catalog.models import *
from baner.models import *
from .models import *
from .forms import *
# Create your views here.

def page_not_found(request):
	category = Category.objects.all()
	return render(request, 'pages/404.html', locals())

def about(request):
	# product = Product.objects.get(id=1)
	# pprint.pprint(product.torg)

	category = Category.objects.all()

	return render(request,'pages/about.html', locals())

def action(request,id):
	# product = Product.objects.get(id=1)
	# pprint.pprint(product.torg)
	category = Category.objects.all()
	sale = Sale.objects.get(id=id)
	popular = Product.objects.filter(hit=True)

	return render(request,'pages/action.html', locals())

def actions(request):
	# product = Product.objects.get(id=1)
	# pprint.pprint(product.torg)
	sale = Sale.objects.filter(pub=True)
	category = Category.objects.all()

	return render(request,'pages/actions.html', locals())

def article(request,id):
	# product = Product.objects.get(id=1)
	# pprint.pprint(product.torg)

	category = Category.objects.all()
	news = News.objects.get(id=id)
	popular = Product.objects.filter(hit=True)
	return render(request,'pages/article.html', locals())

def articles(request):
	# product = Product.objects.get(id=1)
	# pprint.pprint(product.torg)
	category = Category.objects.all()
	news = News.objects.filter(pub=True)


	return render(request,'pages/articles.html', locals())

def contacts(request):
	# product = Product.objects.get(id=1)
	# pprint.pprint(product.torg)
	category = Category.objects.all()


	return render(request,'pages/contacts.html', locals())

def delivery(request):
	# product = Product.objects.get(id=1)
	# pprint.pprint(product.torg)
	category = Category.objects.all()


	return render(request,'pages/delivery.html', locals())

def faq(request):
	# product = Product.objects.get(id=1)
	# pprint.pprint(product.torg)

	category = Category.objects.all()
	faq = Faq.objects.filter(public=True)
	if request.method == 'POST':
		form = FaqForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/faq')
	else:
		form = FaqForm()

	return render(request,'pages/faq.html', locals())

def garantee(request):
	# product = Product.objects.get(id=1)
	# pprint.pprint(product.torg)
	category = Category.objects.all()


	return render(request,'pages/garantee.html', locals())

def index(request):
	# product = Product.objects.get(id=1)
	# pprint.pprint(product.torg)
	# baner = Baner_main.objects.get(id=1)
	category = Category.objects.all()
	news = News.objects.filter(pub=True)
	# lastnews = news[0]
	popular = Product.objects.filter(hit=True)
	new = Product.objects.filter(new=True)
	sale = Product.objects.filter(sale=True)
	return render(request,'pages/index.html', locals())

def notfound(request):
	# product = Product.objects.get(id=1)
	# pprint.pprint(product.torg)

	category = Category.objects.all()

	return render(request,'pages/404.html', locals())



