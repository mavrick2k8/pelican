from django.db import models

# Create your models here.
from catalog.models import *
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator

class DeliveryMetod(models.Model):
	name = models.CharField(verbose_name='Название',max_length=50)
	attr = models.CharField(verbose_name='Атрибут 1',max_length=50)
	attrmetod = models.CharField(verbose_name='Атрибут 2',max_length=50)
	
	class Meta:
		
		verbose_name = 'Доставка'
		verbose_name_plural = 'Варианты доставки'
	
		
		
	def __str__(self):
		return self.name
class OplataMetod(models.Model):
	#order = models.ForeignKey(Order,on_delete='')
	name = models.CharField(verbose_name='Название',max_length=50)
	attr = models.CharField(verbose_name='Атрибут 1',max_length=50)
	
	class Meta:
		
		verbose_name = 'Оплата'
		verbose_name_plural = 'Варианты оплаты'

	def __str__(self):
		return self.name

class Order(models.Model):
	new_name  = models.ForeignKey("lk.User",on_delete='',verbose_name='Пользователь',blank=True,null=True)
	first_name = models.CharField(verbose_name='ФИО', max_length=50,blank=True)
	last_name = models.CharField(verbose_name='Доп. поле', max_length=50,blank=True)
	email = models.EmailField(verbose_name='Email')
	address =  models.CharField(verbose_name='Адрес ', max_length=250)
	# postal_code = models.CharField(verbose_name='Почтовый код', max_length=20)
	city = models.CharField(verbose_name='Город', max_length=100,blank=True)
	created = models.DateTimeField(verbose_name='Создан', auto_now_add=True)
	updated = models.DateTimeField(verbose_name='Обновлен', auto_now=True)
	paid = models.BooleanField(verbose_name='Оплачен', default=False)
	# street = models.CharField(verbose_name='Улица',max_length=150, blank=True)
	# house = models.CharField(verbose_name='Дом',max_length=150, blank=True)
	# apartment = models.CharField(verbose_name='Квартира',max_length=150, blank=True)
	numbers =  models.CharField(verbose_name='Номер телефона', max_length=250,blank=True)
	# cupon = models.ForeignKey(Cupon,on_delete='', related_name='orders', null=True, blank=True,verbose_name='Купон')
	# discount = models.IntegerField(verbose_name='Скидка',default=0, validators=[MinValueValidator(0),MaxValueValidator(100)])
	# 
	comment = models.TextField(verbose_name='Комментарий',blank=True)													  
	order_delivery =  models.ForeignKey(DeliveryMetod,on_delete='',blank=True,null=True,verbose_name='Способ доставки')
	order_payment =  models.ForeignKey(OplataMetod,on_delete='',blank=True,null=True,verbose_name='Способ оплаты')
	class Meta:
		ordering = ('-created', )
		verbose_name = 'Заказ'
		verbose_name_plural = 'Заказы'

	def __str__(self):
		return 'Заказ: {}'.format(self.id)

	def get_delivery(self):
		try:
			delivery_price = Delivery.objects.get(order=self.id)
			price = delivery_price.price
		except:
			price = 0
		return price

	def get_total_cost(self):


		total_cost = sum(item.get_cost() for item in self.items.all())
		# if self.cupon:
		# 	disk = self.cupon.discount
		# 	return total_cost - total_cost * (disk / Decimal('100'))
		# else:
		# 	return total_cost 
		return total_cost 
	
	def get_total_all(self):
		tot = self.total_new 
		delivery = self.deliveri_total
		price = tot +  delivery

		return price 

	deliveri_total = property(get_delivery)
	total_new= property(get_total_cost)
	total_all= property(get_total_all)

class OrderItem(models.Model):
	# order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True, related_name='items',verbose_name='Заказ')
	# product = models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True, null = True, related_name='order_items',verbose_name='Товар')
	# atributeproduct = models.ForeignKey(AtributeProduct,on_delete=models.SET_NULL,blank=True, null = True,verbose_name='Характеристика товара',)
	# price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
	# quantity = models.PositiveIntegerField(verbose_name='Количество', default=1)
	order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True, related_name='items',verbose_name='Заказ')
	product = models.IntegerField(blank=True, null = True,verbose_name='Характеристика товара',)
	product_name = models.CharField(verbose_name='Наименование',max_length=300,blank=True,)
	atributeproduct = models.IntegerField(blank=True, null = True,verbose_name='Характеристика товара')
	atributeproduct_name = models.CharField(verbose_name='Наименование',max_length=300,blank=True)
	price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
	quantity = models.PositiveIntegerField(verbose_name='Количество', default=1)
	link_image = models.CharField(verbose_name='Наименование',max_length=1000,blank=True,)
	# def __str__(self):
	# 	return '{}'.format(self.id)

	def get_cost(self):
		return self.price * self.quantity
	tot_lk= property(get_cost)
	def __str__(self):
		return self.product_name


	


def my_send_email22(zakaz,track,mailto):
		subject = 'Заказ отправлен. Pet-Joy'
		html_message = render_to_string('mail/trackmail.html',{'zakaz':zakaz,'track':track})
		message = ""
		send_mail(subject,
			  settings.EMAIL_HOST_USER,
			  [mailto],
			  html_message=html_message)
	
class Delivery(models.Model):
	order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True,verbose_name='Заказ')
	dostavka = models.ForeignKey(DeliveryMetod,on_delete='',blank=True,null=True,verbose_name='Способ доставки')
	

	# name = models.CharField(max_length=50)## DELETE
	# status = models.CharField(max_length=50)### DELETE
	NEW = 'Новый'
	SEND = 'Отправлен'
	PULL = 'Получен'
	CANCEL = 'Отменен'


	STATUS_NEW  = (
		(NEW, 'Новый'),
		(SEND, 'Отправлен'),
		(PULL, 'Поучен'),
		(CANCEL, 'Отменен'),
	)

	status_new = models.CharField(verbose_name='Статус',max_length=10,
									  choices=STATUS_NEW,
									  default=NEW)

	created = models.DateTimeField(verbose_name='Создан',null=True,blank=True, auto_now_add=True)
	updated = models.DateTimeField(verbose_name='Обновлен',null=True,blank=True, auto_now=True)
	#status_oplati = models.CharField(max_length=50)
	price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
	trackid = models.CharField(verbose_name='Номер отслеживания',max_length=150,blank=True,null=True)
	def __str__(self):
		return self.status_new
	
	def save(self, *args, **kwargs):
		if self.trackid:
			self.status_new = 'Отправлен'
			my_send_email22(self.order.id,self.trackid,self.order.email)
		super(Delivery, self).save(*args, **kwargs)




class Oplata(models.Model):
	###### ДАТА ОПЛАТЫ 
	order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True,verbose_name='Заказ')
	name_new = models.ForeignKey(OplataMetod,on_delete='',blank=True,null=True,verbose_name='Способ оплаты')
	#name = models.CharField(max_length=50)
	#status = models.CharField(max_length=50)
	paid = models.BooleanField(verbose_name='Оплачен', default=False)
	price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2,blank=True,null=True)
	NEW = 'Новый'
	PAID = 'Оплачен'
	RESEND = 'Возврат'
	CANCEL = 'Отменен'
	created = models.DateTimeField(verbose_name='Создан',null=True,blank=True, auto_now_add=True)
	updated = models.DateTimeField(verbose_name='Обновлен',null=True,blank=True, auto_now=True)
	payment_id = models.CharField(verbose_name='ИД Кассы',max_length=720,null=True,blank=True)
	STATUS_NEW  = (
		('NEW', 'Новый'),
		('PAID', 'Оплачен'),
		('RESEND', 'Возврат'),
		('CANCEL', 'Отменен'),
	)

	status_new = models.CharField(verbose_name='Статус оплаты',max_length=10,
									  choices=STATUS_NEW)
	
	class Meta:
		
		verbose_name = 'Оплата'
		verbose_name_plural = 'Оплаты'

	def __str__(self):
		return self.status_new