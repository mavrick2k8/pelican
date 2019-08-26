from django.core.management.base import BaseCommand
from webapp.models import *
import csv
from ftplib import FTP
import re
import pprint
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse

from django.http import JsonResponse
from django.shortcuts import render
import pprint
import requests
import json
import time
class Command(BaseCommand):
	# Задаём текст помощи, который будет
	# отображён при выполнении команды
	# python manage.py createtags --help
	help = 'Export to Joomla'

	# def add_arguments(self, parser):
	#     # Указываем сколько и каких аргументов принимает команда.
	#     # В данном случае, это один аргумент типа int.
	#     parser.add_argument('tags_count', nargs=1, type=int)

	def handle(self, *args, **options):
		# Получаем аргумент, создаём необходимое количество тегов
		# и выводим сообщение об успешном завершении генерирования
		# tags_count = options['tags_count'][0]

		# for i in range(tags_count):
		#     models.Tag.objects.create(text='Tag{0}'.format(i))
		new_id = 10000



		# atributes = Value.objects.filter().distinct()
		# attrlist = []
		# for i in atributes:
		#     key = i.atribute.name
		#     values = i.name


		temp = Value.objects.values('atribute__name','name').filter().order_by('id').distinct()
		keys = []
		temp_dict = {}
		for i in temp:
			if i['atribute__name'] not in keys:
				keys.append(i['atribute__name'])
				temp_dict[i['atribute__name']] = []
				temp_dict[i['atribute__name']].append(i['name'])
			else:
				temp_dict[i['atribute__name']].append(i['name'])
		final_list = []
		for i in temp_dict:
			final_list.append({'key': i,'value': temp_dict[i]})
		# otkud=[]
		atributes = final_list




		#### ВЫГРУЗКА АТРИБУТОВ 
		with open('atr.csv', 'w') as csvfile:
			writer = csv.writer(csvfile)
			# write your header first
			row =( "ID характеристики","Название","Сортировка","Тип","Значение","Категории","Группа")
			writer.writerow(row)
			for obj in atributes:
				znach = str(obj['value'])
				new = znach.replace(",","|")
				new = new.replace("'","")
				new = new.replace("[","")
				new = new.replace("]","")
				new = "zQwe"+new+"zQwe"
				# list_new = 
				
				new_list="Множественный список"
				
				# new_list = new_list.replace("'",'"')
				# new_list = new_list.replace("[","")
				# new_list = new_list.replace("]","")
				new_list = str(new_list)
				new_list = "\'"+new_list+"\'"
				z = "\'"+obj['key']+"\'"
				row = [ 
					"",#"ID характеристики",
					z,#"Название",
					"",#"Сортировка",
					new_list,#"Тип",
					new,#"Значение",
					"",#"Категории",
					"",#"Группа")
					]
				writer.writerow(row)


		#### ВЫГРУЗКА ТОВАРОВ
		getnew = products.objects.filter(category_type__on_site=True)
		

		
		with open('tovar.csv', 'w') as csvfile:
			writer = csv.writer(csvfile)
			# write your header first
			row =( "Название товара",  
			"Псевдоним",   
			# "Код товара",  
			"META заголовок",  
			"META ключевые слова", 
			"META описание",   
			"ID товара",   
			# "URL товара",  
			"Валюта",  
			# "Вес Видео (код)", 
			# "Видео (превью)",  
			# "Видео (файл)",    
			"Дополнительные изображения",  
			"Доступ",  
			# "Единица измерения",   
			# "Закупочная цена", 
			"Категория",   
			"Количество",  
			# "Количество в упаковке",   
			# "Краткое описание",    
			# "Метка",   
			# "Налог",   
			"Описание",    
			"Основное изображение",    
			# "Продавец",    
			"Производитель",   
			"Публикация товара",   
			# "Сопутствующие товары",    
			# "Срок поставки",   
			# "Старая цена", 
			# "Хиты",    
			"Цена",    
			"Шаблон товара",   
			#### ЭТО УЖЕ ПОШЛИ ХАРАКТЕРИСТИКИ ТОВАРА
			# "Диагональ экрана",    
			# "Линейка процессора",  
			# "Оперативная память, Mb",  
			# "Разрешение  Жесткий диск, Gb",    
			# "Наличие SSD", 
			# "Вид графического ускорителя", 
			# "Производитель видеочипа", 
			# "Привод",  
			# "Состояние аккумулятора",  
			# "Состояние",   
			# "Smart TV",    
			# "Поддержка 3D",    
			# "Wi-Fi",   
			# "Видиоразъёмы")
			
			)

		


			for i in keys:
				z = i
				row += (z,)

			#row += ('',)

			writer.writerow(row)
			for obj in getnew:
				pprint.pprint(obj)
				id_tavr = obj.id + new_id
				#Получаем атрибуты товара для записи их в поле описание 
				attr = AtributeProduct.objects.filter(prod=obj)
				desk = "<p> "
				activity = 1
				if obj.quantity == 0:
					activity = 0
				if obj.on_site == False:
					activity = 0
				cati = []
				cati.append(obj.category_type.name)
				def getcategory(cat):
					catigora = category.objects.get(name=cat)
					parent_cat = catigora.parent

					# pprint.pprint(catigora)
					# pprint.pprint(parent_cat)
					#cati.append(g)
					
					if parent_cat:
						cati.append(parent_cat.name)
						getcategory(parent_cat.name)
					

				category_obj = 	obj.category_type
				# z = obj.category_type
				# f = category.objects.get(name=fg)
				getcategory(category_obj)
				# pprint.pprint(cati)

				cati_str = ""
				cati.reverse()
				if len(cati)> 1:
					for i in cati:
						cati_str = cati_str +"/"+ i
				else:
					cati_str = str(cati)
					cati_str = cati_str.replace("'","")
					cati_str = cati_str.replace("[","")
					cati_str = cati_str.replace("]","")
				
				fgh =obj.descriptions
				
				new_desk= fgh.split("\n")
				for i in new_desk:
					g = i.replace("\r","")
					#h = g.replace("/r","")
					#pprint.pprint(g)
					desk += "<span style=""color: #000000; font-family: -apple-system, BlinkMacSystemFont, Roboto, Helvetica Neue, sans-serif; font-size: 13px;""> "+ g+ " "  + "</span>" +'<br/>'+'<br/>'
				#for i in attr:
					# d = i.atributevalue.atribute "," i.atributevalue.name 
					# i.atributevalue.atribute
					# i.atributevalue.name
				#	desk += "<span style=""color: #000000; font-family: -apple-system, BlinkMacSystemFont, Roboto, Helvetica Neue, sans-serif; font-size: 13px;""> "+ str(i.atributevalue.atribute)+ " " + str(i.atributevalue.name) + "</span>" +'<br/>'+'<br/>'
					#desk += 
				if obj.image:
				 	obj.new_image= obj.image.url.split("/")[-1]
				else:
					obj.new_image = ""

				dop_image = SecondImage.objects.filter(prod=obj)

				dop_image_str = ""
				for g in dop_image:
					pprint.pprint(g)
					try:
						dopimg = g.image.url.split("/")[-1]
						dop_image_str += dopimg + ","
					except:
						nothing = 1
				ghj = dop_image_str[:-1]
				row = [  obj.short_descriptions, #"Название товара",  
				obj.short_descriptions,# "Псевдоним",   
				# "Код товара",  
				obj.short_descriptions,#"META заголовок",  
				obj.name,#"META ключевые слова", 
				obj.short_descriptions,#"META описание",   
				id_tavr,#obj.id,#"ID товара",   
				# "URL товара",  
				"руб.",#"Валюта",  
				# "Вес Видео (код)", 
				# "Видео (превью)",  
				# "Видео (файл)",    
				ghj,#"",#"Дополнительные изображения",  
				"Public",#Доступ",  
				# "Единица измерения",   
				# "Закупочная цена", 
				cati_str,#obj.category_type.name,#"TEST",#"Категория",   
				obj.quantity,#"Количество",  
				# "Количество в упаковке",   
				# "Краткое описание",    
				# "Метка",   
				# "Налог",   
				desk,#obj.descriptions,#"Описание",    

				obj.new_image,#"Основное изображение",    
				# "Продавец",    
				"",#"Производитель",   
				activity,#"1",#"Публикация товара",   
				# "Сопутствующие товары",    
				# "Срок поставки",   
				# "Старая цена", 
				# "Хиты",    
				obj.output_price,#"Цена",    
				"default",#"Шаблон товара",   
				#### ЭТО УЖЕ ПОШЛИ ХАРАКТЕРИСТИКИ ТОВАРА
				# "Диагональ экрана",    
				# "Линейка процессора",  
				# "Оперативная память, Mb",  
				# "Разрешение  Жесткий диск, Gb",    
				# "Наличие SSD", 
				# "Вид графического ускорителя", 
				# "Производитель видеочипа", 
				# "Привод",  
				# "Состояние аккумулятора",  
				# "Состояние",   
				# "Smart TV",    
				# "Поддержка 3D",    
				# "Wi-Fi",   
				# "Видиоразъёмы"
				]

				# keys = [ПРОЦЕССОР, ОПЕРАТИВКА,HDD ]
				# temp = [atr1.name= ОПЕРАТИВКА , atr2.name=ПРОЦЕССОР]

				for i in keys:

					row.append(i,)
				#row_new=[]
				for i in attr:
					#pprint.pprint(i.atributevalue.atribute.name)
					for n in range(0,len(row)):
						#row_new.append(n)
						if row[n] == i.atributevalue.atribute.name:
							#pprint.pprint(i.atributevalue.name)
							# f = []
							# f.append(i.atributevalue.name)
							row[n] = i.atributevalue.name
							# pprint.pprint(row[n])
							#row_new.append(i.atributevalue.name)
				 
				# q = len(row) - len(keys)
				# gh = row[-len(keys):]
				for i in keys:
					#pprint.pprint(i.atributevalue.atribute.name)
					for n in range(0,len(row)):
						#row_new.append(n)
						if row[n] == i:
							#pprint.pprint(i.atributevalue.name)
							# f = []
							# f.append(i.atributevalue.name)
							row[n] = ""
							# pprint.pprint(row[n])
							#row_new.append(i.atributevalue.name)

				# cat = []
				# fg = obj.category_type
					# cati = []
					# cati.append(i)
				

				# pprint.pprint(cati_str)
				# if f.parent:


				# pprint.pprint(fg)
				# pprint.pprint(f.parent)
				
				# cati = []
				# for slug in category_slugs:
				# 	if not cati:
				# 		parent = None
				# 	else:
				# 		parent = cati[-1]
				# 	categor = get_object_or_404(category, slug=slug, parent=parent)
				# 	cati.append(categor)
				# pprint.pprint(cati)
				# h = str(row)
				# j = h.replace("SSD",'asdasd')

				#f = list(j)
				# pprint.pprint(j) 

				writer.writerow(row)

		with FTP("bitrix242.timeweb.ru","cs08306","RxoLvos0NZ1c") as ftp:
			# ftp.login()
			ftp.cwd('joomla/public_html/import') 
			# with open('atr.csv', 'rb') as filename:
			# ftp.storlines('atr.csv')
			ftp.storlines('STOR ' + 'atr.csv', open('atr.csv','rb'))
			ftp.storlines('STOR ' + 'tovar.csv', open('tovar.csv','rb'))
			ftp.cwd('images') 
			ftp.dir()
			for i in getnew:
				if i.image:
					mage = i.image.url
					z = str(mage)
					z = z[1:]
					g = mage.split("/")[-1]
					try:
						ftp.storbinary('STOR ' + g, open('/home/c/ch44828/compx/public_html/app/'+z,'rb'))
					except:
						ghf = 1
			ftp.dir()
			ftp.quit()


		host        = "https://2770000.ru/index.php?option=com_jshopping&controller=importexport&task=start&ie_id=3&key=de97975895e362791f251702e96f969a"

		url =  host

		def newimport(url):
			time.sleep(5)
			response = requests.post(url)
			print("Status code: ", response.status_code)
			print("Response body: ", response.text)
			print("Response bodyasdasd: ", response.text[-4:])
			print("Response body: ", response.url)
			if response.text[-4:] == "DONE":
				print("DONE")
				
			else:

				print("NEXTSTEP")
				newimport(response.url)
				
		newimport(url)

		self.stdout.write("OK")