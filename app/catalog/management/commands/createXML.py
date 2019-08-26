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


import xml.etree.ElementTree as xml

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

        
        product = products.objects.filter(on_avito=True)
        root = xml.Element("Ads")
        root.set('formatVersion','3')
        root.set('target','Avito.ru')
        
        
        for i in product:
            ad = xml.SubElement(root, "Ad")
            Id = xml.SubElement(ad, "Id")
            Id.text = str(i.id)
            DateBegin = xml.SubElement(ad, "DateBegin")
            DateBegin.text = "2015-11-27"
            DateEnd = xml.SubElement(ad, "DateEnd")
            DateEnd.text = "2079-08-28"
            AdStatus = xml.SubElement(ad, "AdStatus")
            AdStatus.text = "TurboSale"
            AllowEmail = xml.SubElement(ad, "AllowEmail")
            AllowEmail.text = "Да"
            ManagerName = xml.SubElement(ad, "ManagerName")
            ManagerName.text = "Иван Петров-Водкин"
            ContactPhone = xml.SubElement(ad, "ContactPhone")
            ContactPhone.text = "+7 916 683-78-22"
            Address = xml.SubElement(ad, "Address")
            Address.text = "Россия, Тамбовская область, Моршанск, Лесная улица, 7"
            Category = xml.SubElement(ad, "Category")
            Category.text = str(i.category_type)
            GoodsType = xml.SubElement(ad, "GoodsType")
            GoodsType.text = "Музыкальные центры, магнитолы"
            Title = xml.SubElement(ad, "Title")
            Title.text = str(i.name)
            Description = xml.SubElement(ad, "Description")
            Description.text = "asdasdasd"
            Price = xml.SubElement(ad, "Price")
            Price.text = str(i.output_price)
            Images = xml.SubElement(ad, "Images")
            Image = xml.SubElement(Images, "Image")
            Image.set('url',str(i.image))
            # VideoURL = xml.SubElement(ad, "VideoURL")
            # VideoURL.text = "http://www.youtube.com/watch?v=YKmDXNrDdBI"
        tree = xml.ElementTree(root)
        with open("at.xml", "wb") as fh:
            tree.write(fh,encoding="UTF-8")
        self.stdout.write("OK")