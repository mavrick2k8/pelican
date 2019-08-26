from django.db import models

# Create your models here.
class News(models.Model):
	name  = models.CharField(verbose_name='Заголовок новости',max_length=150)
	short_descriptions = models.TextField(verbose_name='Краткое описание новости',blank=True)
	descriptions = models.TextField(verbose_name='Подробное описание новости',blank=True)
	date_create = models.DateField(auto_now=False, auto_now_add=True)
	pub = models.BooleanField(verbose_name='Публикация')
	image  =  models.ImageField(verbose_name='Картинка новости',blank=True)
	slug = models.SlugField(verbose_name='Ссылка на новость',max_length=200, db_index=True,blank=True)
	###SEO###
	meta_title = models.CharField(verbose_name='META TITLE',max_length=150,blank=True)
	meta_keywords = models.CharField(verbose_name='META KEYWORDS',max_length=150,blank=True)
	meta_descriptions = models.CharField(verbose_name='META DESCRIPTIONS',max_length=150,blank=True)
	class Meta:
		ordering = ['name']
		index_together = [
			['id', 'slug']
		]
		verbose_name = 'Новость'
		verbose_name_plural = 'Новости'
	
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return 'news/'+str(self.id)

class Sale(models.Model):
	name  = models.CharField(verbose_name='Заголовок новости',max_length=150)
	short_descriptions = models.TextField(verbose_name='Краткое описание новости',blank=True)
	descriptions = models.TextField(verbose_name='Подробное описание новости',blank=True)
	date_create = models.DateField(auto_now=False, auto_now_add=True)
	pub = models.BooleanField(verbose_name='Публикация')
	image  =  models.ImageField(verbose_name='Картинка новости',blank=True)
	slug = models.SlugField(verbose_name='Ссылка на новость',max_length=200, db_index=True,blank=True)
	###SEO###
	meta_title = models.CharField(verbose_name='META TITLE',max_length=150,blank=True)
	meta_keywords = models.CharField(verbose_name='META KEYWORDS',max_length=150,blank=True)
	meta_descriptions = models.CharField(verbose_name='META DESCRIPTIONS',max_length=150,blank=True)
	class Meta:
		ordering = ['name']
		index_together = [
			['id', 'slug']
		]
		verbose_name = 'Новость'
		verbose_name_plural = 'Новости'
	
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return 'sale/'+str(self.id)

class Faq(models.Model):
	question = models.TextField(verbose_name='Вопрос',blank=True)
	answer = models.TextField(verbose_name='Ответ',blank=True)
	public = models.BooleanField(blank=True,default=False)
	date_create = models.DateField(auto_now=False, auto_now_add=True)
	e_mail = models.EmailField(verbose_name='Почта',max_length=254)
	name = models.CharField(verbose_name='Имя',max_length=150)

	class Meta:
		verbose_name = 'Вопрос'
		verbose_name_plural = 'Вопросы'
	
	def __str__(self):
		return self.name

