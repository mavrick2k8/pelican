
from django.conf import settings
from .models import *
#from cupons.models import Cupon
import random

class Seelater(object):
	def __init__(self, request):
		# Инициализация корзины пользователя
		self.session = request.session
		#self.cupon_id = self.session.get('cupon_id')
		seelater = self.session.get(settings.SEELATER_SESSION_ID)
		if not seelater:
			# Сохраняем корзину пользователя в сессию
			seelater = self.session[settings.SEELATER_SESSION_ID] = {}
		self.seelater = seelater


	def add(self, keysession):
		ids = keysession
		count = len(self.seelater)
		if count >= 10:
			# fordel = random.choice(self.seelater.keys())
			a = self.seelater
			fordel = a.popitem()
			#del self.seelater[fordel.key]
			self.save()
		if ids not in self.seelater:
			self.seelater[ids] = {'new_id': ids}
		#self.seelater= ids
			self.save()


	def save(self):
		self.session[settings.SEELATER_SESSION_ID] = self.seelater
		# Указываем, что сессия изменена
		self.session.modified = True

	def __iter__(self):
		keysession = self.seelater.keys()
		#products = AtributeProduct.objects.filter(id__in=product_ids)
		# for i in keysession:
		# 	self.cart[i]['product'] = product


		for item in self.seelater.values():
			item['new_id'] = str(item['new_id'])

			yield item
	def clear(self):
		del self.session[settings.SEELATER_SESSION_ID]
		self.session.modified = True

	def remove(self, keysession):
		ids = keysession
		if ids in self.seelater:
			del self.seelater[ids]
			self.save()