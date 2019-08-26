from django.db import models

# Create your models here.
class Baner_main(models.Model):
	# name_id = models.ForeignKey('Clients',blank=True,null=True,on_delete=models.SET_NULL)
	name = models.CharField(verbose_name='Название',max_length=55,blank=True,null=True)
	image = models.ImageField(verbose_name='Банер')
	mobile_image = models.ImageField(verbose_name='Банер мобильная версия',blank=True)
	active = models.BooleanField(verbose_name='Включен')
	link = models.CharField(verbose_name='Ссылка на целевую страницу',max_length=1000,blank=True,null=True)
	class Meta:
		verbose_name = 'Банер главная'
		verbose_name_plural = 'Банеры главная'
	def __str__(self):
		return self.name