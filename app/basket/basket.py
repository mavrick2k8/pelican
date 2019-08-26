from decimal import Decimal
from django.conf import settings
from catalog.models import *
import pprint
class Basket(object):
	def __init__(self, request):
		# Инициализация корзины пользователя
		self.session = request.session
		basket = self.session.get(settings.BASKET_SESSION_ID)
		if not basket:
			# Сохраняем корзину пользователя в сессию
			basket = self.session[settings.BASKET_SESSION_ID] = {}
		self.basket = basket

# Добавление товара в корзину пользователя или обновление количества товара
	def add(self, product, quantity=1, price =None,discount=0):
		#ate = attr
		product_id = product
		if product_id not in self.basket:
			self.basket[product_id] = {'quantity': 0, 'price':0,'discount':discount}
		if product_id in self.basket:
			self.basket[product_id]['quantity'] += int(quantity)
			self.basket[product_id]['price'] = price
		# if update_quantity =='True':
		# 	self.basket[product_id]['quantity'] = int(quantity)
		products = SaleProduct.objects.get(id=product_id)
		self.save()

	# Сохранение данных в сессию
	def save(self):
		self.session[settings.BASKET_SESSION_ID] = self.basket
		# Указываем, что сессия изменена
		self.session.modified = True
	def clear(self):
		del self.session[settings.BASKET_SESSION_ID]
		if self.cupon_id:
			del self.cupon_id
		self.session.modified = True
	def remove(self, product):
		product_id = product
		if product_id in self.basket:
			del self.basket[product_id]
			self.save()

	def __iter__(self):
		products = self.basket.keys()
		prod_ids = SaleProduct.objects.filter(id__in=products)

		for product in prod_ids:
			
			self.basket[str(product.id)]['product'] = product.prod.name
			if product.prod.image.url:
				self.basket[str(product.id)]['image'] = product.prod.image.url
			else:
				self.basket[str(product.id)]['image'] = "no"
			self.basket[str(product.id)]['id'] = product.id
			self.basket[str(product.id)]['name'] = product.name
			# self.basket[str(product.id)]['ves'] = int(product.ves) * 0.001
			# self.basket[str(product.id)]['obem'] = product.obem

		for item in self.basket.values():
			item['price'] = int(item['price'])
			item['quantity'] = int(item['quantity'])
			item['sell_price'] = item['price']
			item['discount_price'] = int(item['price']) * int(item['discount']) / 100
			item['sell_price'] = item['price']  - item['discount_price']
			item['total_price'] = item['sell_price']  * item['quantity']
			pprint.pprint(item)
			yield item

	# Количество товаров
	def __len__(self):
		return sum(item['quantity'] for item in self.basket.values())

	def get_total_price(self):
		return sum(Decimal(item['price']) * item['quantity'] for item in self.basket.values())

	def get_count(self):
		return sum(item['quantity'] for item in self.basket.values())

	basket_count = property(get_count)
	total_basket= property(get_total_price)
	def clear(self):
		del self.session[settings.BASKET_SESSION_ID]
		self.session.modified = True

	@property
	def cupon(self):
		if self.cupon_id:
			return Cupon.objects.get(id=self.cupon_id)
		return None

	def get_discount(self):
		if self.cupon:
			return (self.cupon.discount / Decimal('100')) * self.get_total_price()
		return Decimal('0')

	def get_total_price_after_discount(self):
		return self.get_total_price() - self.get_discount()