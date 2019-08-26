from django.db import models
from django.template.defaultfilters import slugify
import pytils
from django.urls import reverse

# Create your models here.
class Category(models.Model):
	parent = models.ForeignKey('self', blank = True, null = True, related_name="children",on_delete=models.SET_NULL,verbose_name='Родительская категория')
	name  = models.CharField(verbose_name='Категория',max_length=55)
	slug = models.SlugField(verbose_name='Ссылка',max_length=200, db_index=True,blank=True)
	image  =  models.ImageField(verbose_name='Изображение',blank=True)
	descriptions = models.TextField(verbose_name='Описание',blank=True)
	xml_id = models.CharField(verbose_name='Внешний ID',max_length=300,blank=True)
	###SEO###
	meta_title = models.CharField(verbose_name='META TITLE',max_length=150,blank=True)
	meta_keywords = models.CharField(verbose_name='META KEYWORDS',max_length=150,blank=True)
	meta_descriptions = models.CharField(verbose_name='META DESCRIPTIONS',max_length=150,blank=True)
	class Meta:
		unique_together = ('slug', 'parent',)
		verbose_name = 'Категории'
		verbose_name_plural = 'Категории'
		
	def __str__(self):
		if self.parent:
			new_name = self.parent.name + " - " + self.name 
		else:
			new_name = self.name
		return new_name

	# def get_absolute_url(self):
	# 	return reverse('shop:ProductListByCategory', args=[self.slug])
	def get_absolute_url(self):
		h = 'catalog/'
		if self.parent:
			z = self.parent.slug+"/"
			h += z
		h += self.slug
		return h


	def save(self, *args, **kwargs):
		new_sulg = pytils.translit.translify(self.name)
		self.slug = slugify(new_sulg)
		
		super(Category, self).save(*args, **kwargs)

class Brand(models.Model):
	name  = models.CharField(max_length=55)
	image  =  models.ImageField(blank=True)
	###SEO###
	meta_title = models.CharField(verbose_name='META TITLE',max_length=150,blank=True)
	meta_keywords = models.CharField(verbose_name='META KEYWORDS',max_length=150,blank=True)
	meta_descriptions = models.CharField(verbose_name='META DESCRIPTIONS',max_length=150,blank=True)
	xml_id = models.CharField(verbose_name='Внешний ID',max_length=300,blank=True)
	class Meta:
		verbose_name = 'Бренд'
		verbose_name_plural = 'Бренды'

	def __str__(self):
		return self.name 

class Product(models.Model):
	name  = models.CharField(verbose_name='Наименование',max_length=150)
	search_name = models.CharField(verbose_name='Поисковое имя',max_length=150,blank=True,null=True)
	articul = models.CharField(verbose_name='Артикул',max_length=150,blank=True)
	descriptions = models.TextField(verbose_name='Описание',blank=True)
	date_create = models.DateField(auto_now=False, auto_now_add=True)
	sold = models.BooleanField(verbose_name='Продан')
	image  =  models.ImageField(verbose_name='Изображение(если нет характеристики)',blank=True)
	category_type = models.ManyToManyField("Category",blank=True, null = True,verbose_name='Категория')
	brand = models.ForeignKey("Brand",on_delete=models.SET_NULL,blank=True,null=True,verbose_name='Бренд')
	slug = models.SlugField(verbose_name='Ссылка на товар',max_length=200, db_index=True,blank=True)
	hit = models.BooleanField(verbose_name='Хит',default=False)
	new = models.BooleanField(verbose_name='Новинка',default=False)
	sale = models.BooleanField(verbose_name='Распродажа',default=False)
	up = models.BooleanField(verbose_name='Показывать сверху',default=False)
	xml_id = models.CharField(verbose_name='Внешний ID',max_length=300,blank=True)
	###SEO###
	meta_title = models.CharField(verbose_name='META TITLE',max_length=150,blank=True)
	meta_keywords = models.CharField(verbose_name='META KEYWORDS',max_length=150,blank=True)
	meta_descriptions = models.CharField(verbose_name='META DESCRIPTIONS',max_length=150,blank=True)
	class Meta:
		ordering = ['name']
		index_together = [
			['id', 'slug']
		]
		verbose_name = 'Товары'
		verbose_name_plural = 'Товары'
	
	def __str__(self):
		return self.name

	# def get_absolute_url(self):
	# 	  return reverse('shop:ProductDetail', args=[self.id, self.slug])
	def get_absolute_url(self):
		h = self.category_type.all()[0]
		return h.get_absolute_url()+"/"+str(self.id)

	def save(self, *args, **kwargs):
		new_sulg = pytils.translit.translify(self.name)
		self.slug = slugify(new_sulg)
		self.search_name = self.name.upper()
		super(Product, self).save(*args, **kwargs)
	
	def get_sale(self):
		atr = SaleProduct.objects.filter(prod=self.id)
		allpred = SaleAtributeProduct.objects.filter(prod__in=atr)
		return atr

	torg = property(get_sale)
	

	def get_sale1(self):
		atr = SaleProduct.objects.filter(prod=self.id)
		allpred = SaleAtributeProduct.objects.filter(prod__in=atr)
		total = []
		for i in atr:
			tmp = []
			tmp.append(i.name)
			tmp.append(i.price)
			for f in allpred:
				if i == f.prod :
					tmp.append(f.saleatr)
					tmp.append(f.saleatrvalue)
			total.append(tmp)

		return total

	torg1 = property(get_sale1)

class AtributeProduct(models.Model):
	prod = models.ForeignKey("Product",on_delete=models.SET_NULL, null = True,blank=True,verbose_name='Товар')
	atr = models.ForeignKey("Atr",on_delete=models.SET_NULL, null = True,blank=True,verbose_name='Свойство')
	atrvalue = models.ForeignKey("Atrvalue",on_delete=models.SET_NULL, null = True,blank=True,verbose_name='Значение')
	xml_id = models.CharField(verbose_name='Внешний ID',max_length=300,blank=True)
	def __str__(self):
		return self.prod.name

class Atr(models.Model):
	name = models.CharField(verbose_name='Атрибут',max_length=150,blank=True)
	xml_id = models.CharField(verbose_name='Внешний ID',max_length=300,blank=True)

	def __str__(self):
		return self.name
class Atrvalue(models.Model):
	name = models.CharField(verbose_name='Значение атрибута',max_length=150,blank=True)
	xml_id = models.CharField(verbose_name='Внешний ID',max_length=300,blank=True)
	
	def __str__(self):
		return self.name
##### TORG 

class SaleProduct(models.Model):
	prod = models.ForeignKey("Product",on_delete=models.SET_NULL, null = True,blank=True,verbose_name='Товар')
	name  = models.CharField(verbose_name='Наименование',max_length=150)
	price = models.IntegerField(null=True,blank=True)
	image  =  models.ImageField(verbose_name='Изображение',blank=True)
	xml_id = models.CharField(verbose_name='Внешний ID',max_length=300,blank=True)
	quantity = models.SmallIntegerField(verbose_name='Количество',blank=True, null = True)
	class Meta:
		verbose_name = 'Предложения'
		verbose_name_plural = 'Предложение'
	
	def __str__(self):
		return self.name


class SaleAtributeProduct(models.Model):
	prod = models.ForeignKey("SaleProduct",on_delete=models.SET_NULL, null = True,blank=True,verbose_name='Предложение')
	saleatr = models.ForeignKey("SaleAtr",on_delete=models.SET_NULL, null = True,blank=True,verbose_name='Свойство')
	saleatrvalue = models.ForeignKey("SaleAtrvalue",on_delete=models.SET_NULL, null = True,blank=True,verbose_name='Значение')
	xml_id = models.CharField(verbose_name='Внешний ID',max_length=300,blank=True)
	# def __str__(self):
	# 	return self.pk

class SaleAtr(models.Model):
	name = models.CharField(verbose_name='Свойство',max_length=150,blank=True)
	xml_id = models.CharField(verbose_name='Внешний ID',max_length=300,blank=True)

	def __str__(self):
		return self.name
class SaleAtrvalue(models.Model):
	name = models.CharField(verbose_name='Значение свойства',max_length=150,blank=True)
	xml_id = models.CharField(verbose_name='Внешний ID',max_length=300,blank=True)
	
	def __str__(self):
		return self.name
