# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
import pprint
import os
import sys
from catalog.models import *
import xml.etree.ElementTree as ET
import glob
import shutil
class Command(BaseCommand):
	help = 'Import from 1c'
	def handle(self, *args, **options):
		flagfile = True
		
		# try:
			
		# 	# putt = 'C:\\Users\\walder\\Documents\\GitHub\\vsempostel\\vsempostel\\FileDownload\\flag.flag'
		# 	putt = 'C:\\Users\\walder\\Downloads\\forneed\\webdata\\flag.flag'
		# 	fileflagflag = open(putt)
		# 	flagfile = True
		# except:
		# 	flagfile = False
		if flagfile:

			# line = ""
			################# КАТЕГОРИИ ######################
			# cwd = "C:\\Users\\walder\\Documents\\GitHub\\vsempostel\\vsempostel\\FileDownload\\000000002"
			configfiles = glob.glob(r'C:\\Users\\walder\\Downloads\\forneed\\webdata\\*\\*.xml')
			for k in configfiles:
				z = k.split('\\')
				for h in z:
					if h.startswith('import'):
						# pprint.pprint('OK')
						line = k
			tree = ET.parse(line)
			root = tree.getroot()
			for categorys in root.findall('{urn:1C.ru:commerceml_3}Классификатор'):
				groups_categoty = categorys.find('{urn:1C.ru:commerceml_3}Группы')
				category = groups_categoty.findall('{urn:1C.ru:commerceml_3}Группа')
				for cat in category:
					cat_id = cat.find('{urn:1C.ru:commerceml_3}Ид')
					cat_name = cat.find('{urn:1C.ru:commerceml_3}Наименование')
					new_cat = Category.objects.filter(xml_id=cat_id.text)
					if not new_cat:
						cat_new = Category()
						cat_new.name = cat_name.text
						cat_new.xml_id = cat_id.text
						cat_new.save()

			
			# ################## АТРЕБУТЫ ПРЕДЛОЖЕНИЯ ######################
			#cwd = "C:\\Users\\walder\\Documents\\GitHub\\vsempostel\\vsempostel\\FileDownload\\000000002\\properties\\1\\offers___cd493222-09ac-418d-bb11-1f54d3a64166.xml"

			
			# configfiles = glob.glob(r'/home/c/cj27678/import/*/properties/*/*.xml')
			configfiles = glob.glob(r'C:\\Users\\walder\\Downloads\\forneed\\webdata\\*\\properties\\*\\*.xml')
			# pprint.pprint(configfiles)
			# pprint.pprint()
			 

			for k in configfiles:
				z = k.split('\\')
				for h in z:
					if h.startswith('offers'):
						# pprint.pprint('OK')
						line = k
			tree = ET.parse(line)
			root = tree.getroot()
			for i in root.findall('{urn:1C.ru:commerceml_3}Классификатор'):
				atr_groups = i.find('{urn:1C.ru:commerceml_3}Свойства')
				atrs = atr_groups.findall('{urn:1C.ru:commerceml_3}Свойство')
				for atr in atrs:
					atr_id = atr.find('{urn:1C.ru:commerceml_3}Ид')
					atr_name = atr.find('{urn:1C.ru:commerceml_3}Наименование')
					old_atr = SaleAtr.objects.filter(xml_id=atr_id.text)
					if not old_atr:
						new_atr = SaleAtr()
						new_atr.name = atr_name.text
						new_atr.xml_id = atr_id.text
						new_atr.save()

					values_group = atr.find('{urn:1C.ru:commerceml_3}ВариантыЗначений')
					values = values_group.findall('{urn:1C.ru:commerceml_3}Справочник')
					for value in values_group:
						value_id = value.find('{urn:1C.ru:commerceml_3}ИдЗначения')
						value_name = value.find('{urn:1C.ru:commerceml_3}Значение')
						old_value = SaleAtrvalue.objects.filter(xml_id=value_id.text)
						if not old_value:
							new_value = SaleAtrvalue()
							new_value.name = value_name.text
							new_value.xml_id = value_id.text
							new_value.save()
			# self.stdout.write("OK")
	# ################## АТРЕБУТЫ ТОВАРА ######################
			#cwd = "C:\\Users\\walder\\Documents\\GitHub\\vsempostel\\vsempostel\\FileDownload\\000000002\\properties\\1\\import___4151b1c3-907a-4716-80a6-d3f5df84d92a.xml"
			# configfiles = glob.glob(r'/home/c/cj27678/import/*/properties/*/*.xml')
			configfiles = glob.glob(r'C:\\Users\\walder\\Downloads\\forneed\\webdata\\*\\properties\\*\\*.xml')
			# pprint.pprint(configfiles)
			# pprint.pprint()
			 

			for k in configfiles:
				z = k.split('\\')
				for h in z:
					if h.startswith('import'):
						# pprint.pprint('OK')
						line = k
			tree = ET.parse(line)
			root = tree.getroot()
			for i in root.findall('{urn:1C.ru:commerceml_3}Классификатор'):
				atr_groups = i.find('{urn:1C.ru:commerceml_3}Свойства')
				atrs = atr_groups.findall('{urn:1C.ru:commerceml_3}Свойство')
				for atr in atrs:
					atr_id = atr.find('{urn:1C.ru:commerceml_3}Ид')
					atr_name = atr.find('{urn:1C.ru:commerceml_3}Наименование')
					old_atr = Atr.objects.filter(xml_id=atr_id.text)
					if not old_atr:
						new_atr = Atr()
						new_atr.name = atr_name.text
						new_atr.xml_id = atr_id.text
						new_atr.save()
					values_group = atr.find('{urn:1C.ru:commerceml_3}ВариантыЗначений')
					values = values_group.findall('{urn:1C.ru:commerceml_3}Справочник')
					for value in values:
						value_id = value.find('{urn:1C.ru:commerceml_3}ИдЗначения')
						value_name = value.find('{urn:1C.ru:commerceml_3}Значение')

						old_value = Atrvalue.objects.filter(xml_id=value_id.text)
						if not old_value:
							new_value = Atrvalue()
							new_value.name = value_name.text
							new_value.xml_id = value_id.text
							new_value.save()
			# ##################  ТОВАР ######################
			falseall = Product.objects.filter(sold=False)
			for i in falseall:
				i.sold = True
				i.save()
			#cwd = "C:\\Users\\walder\\Documents\\GitHub\\vsempostel\\vsempostel\\FileDownload\\000000002\\goods\\1\\import___9ab51e5a-523b-4728-a5d9-d22179947358.xml"
			# configfiles = glob.glob(r'/home/c/cj27678/import/*/goods/*/*.xml')
			configfiles = glob.glob(r'C:\\Users\\walder\\Downloads\\forneed\\webdata\\*\\goods\\*\\*.xml')
			# pprint.pprint(configfiles)
			# pprint.pprint()
			 

			for k in configfiles:
				z = k.split('\\')
				for h in z:
					if h.startswith('import'):
						pprint.pprint('OK')
						line = k
			tree = ET.parse(line)
			# tree = ET.parse(cwd)
			root = tree.getroot()
			for catalog in root.findall('{urn:1C.ru:commerceml_3}Каталог'):
				products = catalog.find('{urn:1C.ru:commerceml_3}Товары')
				product = products.findall('{urn:1C.ru:commerceml_3}Товар')
				# pprint.pprint(fff)
				for obj in product:
					###### ТОВАР
					product_id = obj.find('{urn:1C.ru:commerceml_3}Ид')
					product_name = obj.find('{urn:1C.ru:commerceml_3}Наименование')
					product_description =obj.find('{urn:1C.ru:commerceml_3}Описание') 
					product_image =obj.find('{urn:1C.ru:commerceml_3}Картинка')
					pprint.pprint(product_name.text)
					pprint.pprint(product_id.text)
					####### КАТЕГОРИЯ ТОВАРА
					groups = obj.find('{urn:1C.ru:commerceml_3}Группы')
					group = groups.find('{urn:1C.ru:commerceml_3}Ид')
					pprint.pprint(group.text)
					####### ДОБВАЛЯЕМ ТОВАР 
					# new_prod = Product.objects.filter(xml_id=product_id.text)
					try:
						prod = Product.objects.get(xml_id=product_id.text)

					except:
						prod = Product()
					prod.name = product_name.text
					prod.xml_id = product_id.text
					if product_description.text:
						prod.descriptions = product_description.text
					prod.sold = False
					
					prod.save()
					cat = Category.objects.get(xml_id=group.text)
					prod.category_type.add(cat)
					# gfh = product_image.text.split('.')
					# images = str(prod.id)+'.' +gfh[-1]
					# f = open('C:\\Users\\walder\\Downloads\\forneed\\webdata\\000000001\\goods\\1\\'+product_image.text, 'rb')
					
					# prod.image.save(images,f,save=True)
					prod.save()

					####### СВОЙСТВА ТОВАРА 
					atr_group = obj.find('{urn:1C.ru:commerceml_3}ЗначенияСвойств')
					atrs = atr_group.findall('{urn:1C.ru:commerceml_3}ЗначенияСвойства')
					for atr in atrs:
						atr_id = atr.find('{urn:1C.ru:commerceml_3}Ид')
						value_id = atr.find('{urn:1C.ru:commerceml_3}Значение')
						pprint.pprint(atr_id.text)
						pprint.pprint(value_id.text)
						pr = Product.objects.get(xml_id=product_id.text)
						new_atr = AtributeProduct.objects.filter(prod=pr,atr__xml_id=atr_id.text,atrvalue__xml_id=value_id.text)
						if not new_atr:
							try:
								atr_prod = AtributeProduct()
								atr_prod.prod = pr
								atr_prod.atr = Atr.objects.get(xml_id=atr_id.text)
								atr_prod.atrvalue = Atrvalue.objects.get(xml_id=value_id.text)
								atr_prod.save()
							except:
								f=0

			################# ПРЕДЛОЖЕНИЯ
			# cwd = "C:\\Users\\walder\\Documents\\GitHub\\vsempostel\\vsempostel\\FileDownload\\000000002\\goods\\1\\offers___77cd1cfe-1edb-4979-acbf-302717f96033.xml"
			# configfiles = glob.glob(r'/home/c/cj27678/import/*/goods/*/*.xml')
			configfiles = glob.glob(r'C:\\Users\\walder\\Downloads\\forneed\\webdata\\*\\goods\\*\\*.xml')
			# pprint.pprint(configfiles)
			# pprint.pprint()
			 

			for k in configfiles:
				z = k.split('\\')
				for h in z:
					if h.startswith('offers'):
						pprint.pprint('OK')
						line = k
			tree = ET.parse(line)
			# tree = ET.parse(cwd)
			root = tree.getroot()
			for i in root.findall('{urn:1C.ru:commerceml_3}ПакетПредложений'):
				atr_groups = i.find('{urn:1C.ru:commerceml_3}Предложения')
				atrs = atr_groups.findall('{urn:1C.ru:commerceml_3}Предложение')
				for atr in atrs:
					atr_id = atr.find('{urn:1C.ru:commerceml_3}Ид')
					atr_name = atr.find('{urn:1C.ru:commerceml_3}Наименование')
					old_atr = SaleProduct.objects.filter(xml_id=atr_id.text)
					pr = atr_id.text.split("#")
					if not old_atr:
						# pr = atr_id.text.split("#")
						new_atr = SaleProduct()
						new_atr.name = atr_name.text
						new_atr.xml_id = atr_id.text
						new_atr.prod = Product.objects.get(xml_id=pr[0])
						new_atr.save()
					pprint.pprint(atr_id.text)
					pprint.pprint(atr_name.text)
					values_group = atr.find('{urn:1C.ru:commerceml_3}ЗначенияСвойств')
					try:
						values = values_group.findall('{urn:1C.ru:commerceml_3}ЗначенияСвойства')
						for value in values:
							value_id = value.find('{urn:1C.ru:commerceml_3}Ид')
							value_name = value.find('{urn:1C.ru:commerceml_3}Значение')
							# pprint.pprint(value_id.text)
							# pprint.pprint(pr[0])
							old = SaleProduct.objects.get(xml_id=atr_id.text)
							# pprint.pprint('1')
							old_atr = SaleAtr.objects.get(xml_id=value_id.text)
							old_value = SaleAtrvalue.objects.get(xml_id=value_name.text)
							# pprint.pprint(old_atr)
							old_atrsale = SaleAtributeProduct.objects.filter(prod=old,saleatr=old_atr,saleatrvalue=old_value)
							if not old_atrsale:
								new_value = SaleAtributeProduct()
								new_value.prod = old
								new_value.saleatr = old_atr
								new_value.saleatrvalue = old_value
								new_value.save()
					except:
						s = 0

			################ ЦЕНЫ
			# cwd = "C:\\Users\\walder\\Documents\\GitHub\\vsempostel\\vsempostel\\FileDownload\\000000002\\goods\\1\\prices___df443a48-c934-4d91-9653-e2aafa7c70d3.xml"
			# configfiles = glob.glob(r'/home/c/cj27678/import/*/goods/*/*.xml')
			configfiles = glob.glob(r'C:\\Users\\walder\\Downloads\\forneed\\webdata\\*\\goods\\*\\*.xml')
			# pprint.pprint(configfiles)
			# pprint.pprint()
			 

			for k in configfiles:
				z = k.split('\\')
				for h in z:
					if h.startswith('prices'):
						pprint.pprint('OK')
						line = k
			tree = ET.parse(line)
			# tree = ET.parse(cwd)
			root = tree.getroot()
			for i in root.findall('{urn:1C.ru:commerceml_3}ПакетПредложений'):
				atr_groups = i.find('{urn:1C.ru:commerceml_3}Предложения')
				atrs = atr_groups.findall('{urn:1C.ru:commerceml_3}Предложение')
				for atr in atrs:
					atr_id = atr.find('{urn:1C.ru:commerceml_3}Ид')
					# atr_name = atr.find('{urn:1C.ru:commerceml_3}Наименование')
					# old_atr = SaleProduct.objects.filter(xml_id=atr_id.text)
					pprint.pprint(atr_id.text)
					new_sale = SaleProduct.objects.get(xml_id=atr_id.text)
					# if not old_atr:
						# pr = atr_id.text.split("#")
						# new_atr = SaleProduct()
						# new_atr.name = atr_name.text
						# new_atr.xml_id = atr_id.text
						# new_atr.prod = Product.objects.get(xml_id=pr[0])
						# new_atr.save()
					# pprint.pprint(atr_id.text)
					# pprint.pprint(atr_name.text)
					values_group = atr.find('{urn:1C.ru:commerceml_3}Цены')
					try:
						values = values_group.findall('{urn:1C.ru:commerceml_3}Цена')
						for value in values:
							value_id = value.find('{urn:1C.ru:commerceml_3}ЦенаЗаЕдиницу')
							# value_name = value.find('{urn:1C.ru:commerceml_3}Значение')
							pprint.pprint(value_id.text)
							new_sale.price = value_id.text
							new_sale.save()
							# pprint.pprint(value_name.text)
							# old_value = Atrvalue.objects.filter(xml_id=value_id.text)
							# if not old_value:
							# 	new_value = Atrvalue()
							# 	new_value.name = value_name.text
							# 	new_value.xml_id = value_id.text
							# 	new_value.save()
					except:
						s = 0

			################## КОЛИЧЕСТВ
			#cwd = "C:\\Users\\walder\\Documents\\GitHub\\vsempostel\\vsempostel\\FileDownload\\000000002\\goods\\1\\rests___3438e28a-fd3c-4282-8cd1-9d8e2f72d5de.xml"
			# configfiles = glob.glob(r'/home/c/cj27678/import/*/goods/*/*.xml')
			configfiles = glob.glob(r'C:\\Users\\walder\\Downloads\\forneed\\webdata\\*\\goods\\*\\*.xml')
			# pprint.pprint(configfiles)
			# pprint.pprint()
			 

			for k in configfiles:
				z = k.split('\\')
				for h in z:
					if h.startswith('rest'):
						pprint.pprint('OK')
						line = k
			tree = ET.parse(line)
			#tree = ET.parse(cwd)
			root = tree.getroot()
			for i in root.findall('{urn:1C.ru:commerceml_3}ПакетПредложений'):
				atr_groups = i.find('{urn:1C.ru:commerceml_3}Предложения')
				atrs = atr_groups.findall('{urn:1C.ru:commerceml_3}Предложение')
				for atr in atrs:
					atr_id = atr.find('{urn:1C.ru:commerceml_3}Ид')
					# atr_name = atr.find('{urn:1C.ru:commerceml_3}Наименование')
					# old_atr = SaleProduct.objects.filter(xml_id=atr_id.text)
					pprint.pprint(atr_id.text)
					new_sale = SaleProduct.objects.get(xml_id=atr_id.text)
					# if not old_atr:
						# pr = atr_id.text.split("#")
						# new_atr = SaleProduct()
						# new_atr.name = atr_name.text
						# new_atr.xml_id = atr_id.text
						# new_atr.prod = Product.objects.get(xml_id=pr[0])
						# new_atr.save()
					# pprint.pprint(atr_id.text)
					# pprint.pprint(atr_name.text)
					values_group = atr.find('{urn:1C.ru:commerceml_3}Остатки')
					try:
						values = values_group.findall('{urn:1C.ru:commerceml_3}Остаток')
						for value in values:
							value_id = value.find('{urn:1C.ru:commerceml_3}Количество')
							# value_name = value.find('{urn:1C.ru:commerceml_3}Значение')
							pprint.pprint(value_id.text)
							new_sale.quantity = value_id.text
							new_sale.save()
							# pprint.pprint(value_name.text)
							# old_value = Atrvalue.objects.filter(xml_id=value_id.text)
							# if not old_value:
							# 	new_value = Atrvalue()
							# 	new_value.name = value_name.text
							# 	new_value.xml_id = value_id.text
							# 	new_value.save()
					except:
						s = 0
			os.remove(putt)


			# shutil.rmtree('/home/c/cj27678/import/000000002')


		else:
			s = 0 
			pprint.pprint('not oj')
			# mydir= raw_input("C:\\Users\\walder\\Documents\\GitHub\\vsempostel\\vsempostel\\FileDownload\\000000002")
			# shutil.rmtree(mydir)

		self.stdout.write("OK")



 

