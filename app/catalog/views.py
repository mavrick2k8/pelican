from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
from .models import *
from pages.models import *
from django.db.models import Avg, Max, Min
import pprint
from .seelater import * 
from django.conf import settings
def categories(request):
	category = Category.objects.all()
	popular = Product.objects.filter(hit=True,sold=False)
	new = Product.objects.filter(new=True,sold=False)
	sale = Product.objects.filter(sale=True,sold=False)
	news = News.objects.filter(pub=True)
	lastnews = news[0]
	return render(request,'catalog/categories.html', locals())

def product_detail(request,hierarchy,pk):

	category = Category.objects.all()
	product = Product.objects.get(id=pk)
	category_slugs = hierarchy.split('/')
	category_slug = category_slugs[-1]
	s = Category.objects.get(slug=category_slug)
	popular = Product.objects.filter(hit=True)
	seelater = Seelater(request)
	last_id = []
	for z in seelater:
		last_id.append(z["new_id"])
	lastview = Product.objects.filter(id__in=last_id)

	seelater.add(keysession=pk)
	return render(request,'catalog/item.html', locals())

# def find(request):
# 	category = Category.objects.all()
# 	brand = Brand.objects.filter()
# 	# products = Product.objects.filter()
# 	if request.method == 'POST':
# 		if "key"in request.POST: 
# 			data = request.POST
# 			prod_list = data['key']
# 			products = Product.objects.filter(name__contains=prod_list)
			
# 			return render(request,'catalog/item_list.html', locals())

# 	return render(request,'catalog/item_list.html', locals())

def find(request):
	category = Category.objects.all()
	brand = Brand.objects.filter()
	prod_list = []
	products = Product.objects.filter(name__contains=prod_list,sold=False)
			### PAGINATOR
	paginator = Paginator(products, 8)
	page = request.GET.get('page')
	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		products = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		products = paginator.page(paginator.num_pages)

	# products = Product.objects.filter()
	if request.method == 'POST':
		if "key"in request.POST: 
			data = request.POST
			prod_list = data['key']
			products = Product.objects.filter(sold=False,name__contains=prod_list)
			### PAGINATOR
			paginator = Paginator(products, 8)
			page = request.GET.get('page')
			try:
				products = paginator.page(page)
			except PageNotAnInteger:
				# If page is not an integer, deliver first page.
				products = paginator.page(1)
			except EmptyPage:
				# If page is out of range (e.g. 9999), deliver last page of results.
				products = paginator.page(paginator.num_pages)

			return render(request,'catalog/item_list.html', locals())

	return render(request,'catalog/item_list.html', locals())

# def product_list(request,hierarchy=None):
	
# 	category = Category.objects.all()
# 	brand = Brand.objects.filter()
	
# 	if hierarchy:
# 		category_slugs = hierarchy.split('/')
# 		category_slug = category_slugs[-1]
# 		s = Category.objects.get(slug=category_slug)
# 		category = Category.objects.filter()
# 		price_avg = SaleProduct.objects.filter(prod__category_type=s).aggregate(Avg('price'), Max('price'), Min('price'))
# 		price_min1 = price_avg['price__min']
# 		price_max1 = price_avg['price__max']
# 		products = Product.objects.filter(category_type=s)
# 		tabar = AtributeProduct.objects.filter(prod__category_type=s).values('atr__name',
# 			'atrvalue__name').filter().order_by('atr__name').distinct()
# 		data = request.GET
# 		if data: 
# 			new_list = []
# 			new1_list = []
# 			for i in data:
# 				if i !='min' and i != 'max' :
# 					new_list.append(i)
# 					new1_list.append(data.getlist(i))
# 			temp =[]
# 			for i in new1_list:
# 				for j in i:
# 					temp.append(j)
# 			new1_list = temp
# 			price_min = data['min']
# 			price_max = data['max']
# 			if  new1_list and  new_list:
# 				products = Product.objects.filter(category_type=s,atributeproduct__atrvalue__name__in=new1_list,
# 					atributeproduct__atr__name__in=new_list,saleproduct__price__range=(price_min,price_max)).distinct()
# 			else:
# 				products = Product.objects.filter(saleproduct__price__range=(price_min,price_max)).distinct()
# 	else:
# 		products = Product.objects.filter()
# 		category = Category.objects.filter()
# 		price_avg = SaleProduct.objects.filter().aggregate(Avg('price'), Max('price'), Min('price'))
# 		price_min1 = price_avg['price__min']
# 		price_max1 = price_avg['price__max']
# 		tabar = AtributeProduct.objects.values('atr__name',
# 			'atrvalue__name').filter().order_by('atr__name').distinct()
# 	return render(request,'catalog/item_list.html', locals())

def product_list(request,hierarchy=None):
	
	category = Category.objects.all()
	brand = Brand.objects.filter()
	
	if hierarchy:
		category_slugs = hierarchy.split('/')
		category_slug = category_slugs[-1]
		s = Category.objects.get(slug=category_slug)
		category = Category.objects.filter()
		price_avg = SaleProduct.objects.filter(prod__category_type=s).aggregate(Avg('price'), Max('price'), Min('price'))
		price_min1 = price_avg['price__min']
		price_max1 = price_avg['price__max']
		products = Product.objects.filter(category_type=s,sold=False)
		tabar = AtributeProduct.objects.filter(prod__category_type=s).values('atr__name',
			'atrvalue__name').filter().order_by('atr__name').distinct()
		paginator = Paginator(products, 16)
		page = request.GET.get('page')
		try:
			products = paginator.page(page)
		except PageNotAnInteger:
			# If page is not an integer, deliver first page.
			products = paginator.page(1)
		except EmptyPage:
			# If page is out of range (e.g. 9999), deliver last page of results.
			products = paginator.page(paginator.num_pages)


		try:
			data = request.GET
			if data: 
				new_list = []
				new1_list = []
				for i in data:
					if i !='min' and i != 'max' :
						new_list.append(i)
						new1_list.append(data.getlist(i))
				temp =[]
				for i in new1_list:
					for j in i:
						temp.append(j)
				new1_list = temp
				price_min = data['min']
				price_max = data['max']
				if  new1_list and  new_list:
					products = Product.objects.filter(sold=False,category_type=s,atributeproduct__atrvalue__name__in=new1_list,
						atributeproduct__atr__name__in=new_list,saleproduct__price__range=(price_min,price_max)).distinct()
				else:
					products = Product.objects.filter(sold=False,saleproduct__price__range=(price_min,price_max)).distinct()

				# paginator = Paginator(products, 8)
				# page = request.GET.get('page')
				# try:
				# 	products = paginator.page(page)
				# except PageNotAnInteger:
				# 	# If page is not an integer, deliver first page.
				# 	products = paginator.page(1)
				# except EmptyPage:
				# 	# If page is out of range (e.g. 9999), deliver last page of results.
				# 	products = paginator.page(paginator.num_pages)
		except:
			s =0
	else:
		products = Product.objects.filter(sold=False)
		category = Category.objects.filter()
		price_avg = SaleProduct.objects.filter().aggregate(Avg('price'), Max('price'), Min('price'))
		price_min1 = price_avg['price__min']
		price_max1 = price_avg['price__max']
		tabar = AtributeProduct.objects.values('atr__name',
			'atrvalue__name').filter().order_by('atr__name').distinct()

	return render(request,'catalog/item_list.html', locals())