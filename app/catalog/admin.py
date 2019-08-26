from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Category)
admin.site.register(Brand) 
# admin.site.register(Product)


class ZakazProductsInline(admin.TabularInline):
	model = AtributeProduct
	raw_id_field = ['id']
class Zakaz2ProductsInline(admin.TabularInline):
	model = SaleProduct
	raw_id_field = ['id']
class ZakazAdmin(admin.ModelAdmin):
	list_filter = ['sold','hit','new','sale','category_type',]
	inlines = [ZakazProductsInline,Zakaz2ProductsInline]
	search_fields = ['name']
	# list_display = ['id', 'name', 'articul','date_create','sold','hit','new','sale_main']
	# prepopulated_fields = {'slug': ('name', )}
admin.site.register(Product,ZakazAdmin)
admin.site.register(AtributeProduct)
admin.site.register(Atr)
admin.site.register(Atrvalue)


class Zakaz1ProductsInline(admin.TabularInline):
	model = SaleAtributeProduct
	raw_id_field = ['id']

class Zakaz1Admin(admin.ModelAdmin):
	inlines = [Zakaz1ProductsInline]
	search_fields = ['name']
	# list_display = ['id', 'name', 'articul','date_create','sold','hit','new','sale_main']
	# prepopulated_fields = {'slug': ('name', )}
admin.site.register(SaleProduct,Zakaz1Admin)
admin.site.register(SaleAtributeProduct)
admin.site.register(SaleAtr)
admin.site.register(SaleAtrvalue)

