# -*- coding: utf-8 -*-

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

import requests
import json
import time
from lxml import etree

import xml.etree.ElementTree as xml

class Command(BaseCommand):
	# Задаём текст помощи, который будет
	# отображён при выполнении команды
	# python manage.py createtags --help
	help = 'Avito export'

	# def add_arguments(self, parser):
	#     # Указываем сколько и каких аргументов принимает команда.
	#     # В данном случае, это один аргумент типа int.
	#     parser.add_argument('tags_count', nargs=1, type=int)


   
	def handle(self, *args, **options):
		category_dict= {
		4:"Товары для компьютера",
		3:"Игры, приставки и программы",
		1:"Ноутбуки",
		2:"Настольные компьютеры",
		16:"Настольные компьютеры",
		31:"Настольные компьютеры",
		9:"Настольные компьютеры",
		5:"Товары для компьютера",
		20:"Товары для компьютера",
		43:"Товары для компьютера",
		23:"Товары для компьютера",
		24:"Товары для компьютера",
		38:"Товары для компьютера",
		39:"Товары для компьютера",
		41:"Товары для компьютера",
		44:"Товары для компьютера",
		6:"Товары для компьютера",
		10:"Товары для компьютера",
		11:"Товары для компьютера",
		21:"Товары для компьютера",
		12:"Ноутбуки",
		15:"Планшеты и электронные книги",
		14:"Телефоны",
		13:"Аудио и видео",
		42:"Оргтехника и расходники",
		8:"Фототехника",
		}

		sub_category_dict={
		20:"Оперативная память",
		43:"Оперативная память",
		4:"Мониторы",
		3:"Игровые приставки",
		24:"Процессоры",
		38:"Материнские платы",
		39:"Блоки питания",
		41:"Корпусы",
		44:"Блоки питания",
		6:"Видеокарты",
		10:"Жёсткие диски",
		11:"Жёсткие диски",
		21:"Жёсткие диски",
		15:"Планшеты",
		42:"МФУ, копиры и сканеры",
		13:"Телевизоры и проекторы",
		8:"Зеркальные фотоаппараты",
		}
		comp_list = [ 'Acer','Apple','ASUS','Compaq','Dell','Fujitsu','HP','Lenovo','MSI','Microsoft','Samsung','Sony','Toshiba','Packard Bell']
		product = products.objects.filter(on_avito=True)
		tel_list = ['Acer','Alcatel','ASUS','BlackBerry','BQ','DEXP','Explay','Fly','Highscreen','HTC','Huawei','iPhone','Lenovo','LG','Meizu','Micromax','Microsoft','Motorola','MTS','Nokia','Panasonic','Philips','Prestigio','Samsung','Siemens','SkyLink','Sony','teXet','Vertu','Xiaomi','ZTE']

		# Создание корневого элемента html
		page = etree.Element('Ads', formatVersion="3" ,target="Avito.ru")

		for i in product:
			# Добавление двух дочерних элементов - <head> и <body>
			headElt = etree.SubElement(page, 'Ad')
			# bodyElt = etree.SubElement(page, 'body')

			# Пример: добавление элемента <title>Your page title here</title>
			title = etree.SubElement(headElt, 'Id')
			title.text = str(i.id)

			title = etree.SubElement(headElt, 'DateBegin')
			# title.text = "2015-11-27"

			title = etree.SubElement(headElt, 'DateEnd')
			# title.text = "2015-11-27"

			title = etree.SubElement(headElt, 'AdStatus')
			title.text = "Free"

			title = etree.SubElement(headElt, 'AllowEmail')
			title.text = "Да"

			title = etree.SubElement(headElt, 'ManagerName')
			title.text = "Александр"

			title = etree.SubElement(headElt, 'ContactPhone')
			title.text = "83832770000"

			title = etree.SubElement(headElt, 'Address')
			title.text = "Новосибирск, проспект Карла Маркса, 14"

			title = etree.SubElement(headElt, 'Category')

			z = category_dict.get(i.category_type.id)
			if z :
				title.text = str(z)
			

			title = etree.SubElement(headElt, 'GoodsType')
			f = sub_category_dict.get(i.category_type.id)
			if f :
				title.text  = str(f)
			else:
				if i.category_type.id == 12 or i.category_type.id == 1:
					title.text = "Другой"
				if i.category_type.id == 14:
							if title.text not in tel_list:
								title.text = "Другие марки"
			g = i.category_type.id
			if g == 1:
				

				z = AtributeProduct.objects.filter(prod=i,atributevalue__atribute__id=6)
				if z:
					for j in z:
						title.text = j.atributevalue.name
						if i.category_type.id == 12 or i.category_type.id == 1:
							if title.text not in comp_list:
								title.text = "Другой"
						if i.category_type.id == 14:
							if title.text not in tel_list:
								title.text = "Другие марки"
				else:
					title.text = "Другой"
				

			title = etree.SubElement(headElt, 'Title')
			title.text = str(i.short_descriptions)

			title = etree.SubElement(headElt, 'Description')

			attrib = AtributeProduct.objects.filter(prod=i)
			desk = i.descriptions
			# pprint.pprint()
			go = ""
			tempz = desk.split('\n')

			for k in tempz:
				go+= "<p>"+ k +"</p>"
			# for k in attrib:
			#         # d = i.atributevalue.atribute "," i.atributevalue.name 
			#         # i.atributevalue.atribute
			#         # i.atributevalue.name
			#         hot = ""

			#         if k.atributevalue.atribute.id == 4 or k.atributevalue.atribute.id == 3: 
			#             hot += "GB"
			#         if k.atributevalue.atribute.id == 2: 
			#             hot += "Mb"
			#         desk += "<p>"+ str(k.atributevalue.atribute)+ " - " + str(k.atributevalue.name) +" " + hot+"</p>"
			teting = "<p>30 дней на полную проверку ноутбука и год сервисного обслуживания от магазина.</p><p>Кредит, безнал.</p><p>Если вас заинтересовал этот товар, позвоните ꟷ Будем рады Вам помочь.</p><p>Мы находимся по адресу: Проспект Карла Маркса 14, магазин CompX. Работаем 7 дней в неделю с 10.00 до 20.00</p>"
			new_str = "<p>------------------------------------------------------------------------------------</p><p>Гарантия: до 3 мес,1 год сервисного обслуживания.</p><p>------------------------------------------------------------------------------------</p><p>Возможно приобрести в рассрочку или кредит!</p><p>------------------------------------------------------------------------------------</p><p>Принимаем в зачет Вашу старую технику (ноутбуки, компьютеры)</p><p>------------------------------------------------------------------------------------</p><p>Возможна доставка!</p><p>------------------------------------------------------------------------------------</p><p>Мы находимся по адресу: Проспект Карла Маркса, 14.</p><p>Часы работы: без обеда и выходных с 10:00 до 20:00. Широкий ассортимент подержанных ноутбуков и компьютеров.</p>"

			title.text = etree.CDATA(go+new_str)

			title = etree.SubElement(headElt, 'Price')
			title.text = str(i.output_price)

			titleIm = etree.SubElement(headElt, 'Images')
			

			
			
			if i.image:
				title = etree.SubElement(titleIm, 'Image',url="http://compx.tlab-nsk.ru/static/media/"+str(i.image))
			dop_image = SecondImage.objects.filter(prod=i)
			for j in dop_image:
				title = etree.SubElement(titleIm, 'Image',url="http://compx.tlab-nsk.ru/static/media/"+str(j.image))

		# Создание и сохранение документа
		doc = etree.ElementTree(page)
		outFile = open('/home/c/ch44828/compx/public_html/app/static/media/exportavito.xml', 'wb')
		#outFile = open('exportavito.xml', 'wb')
		doc.write(outFile,encoding="UTF-8")



		self.stdout.write("OK")