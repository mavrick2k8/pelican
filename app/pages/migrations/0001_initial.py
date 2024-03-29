# Generated by Django 2.0 on 2019-07-18 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Заголовок новости')),
                ('short_descriptions', models.TextField(blank=True, verbose_name='Краткое описание новости')),
                ('descriptions', models.TextField(blank=True, verbose_name='Подробное описание новости')),
                ('date_create', models.DateField(auto_now_add=True)),
                ('pub', models.BooleanField(verbose_name='Публикация')),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='Картинка новости')),
                ('slug', models.SlugField(blank=True, max_length=200, verbose_name='Ссылка на новость')),
                ('meta_title', models.CharField(blank=True, max_length=150, verbose_name='META TITLE')),
                ('meta_keywords', models.CharField(blank=True, max_length=150, verbose_name='META KEYWORDS')),
                ('meta_descriptions', models.CharField(blank=True, max_length=150, verbose_name='META DESCRIPTIONS')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Заголовок новости')),
                ('short_descriptions', models.TextField(blank=True, verbose_name='Краткое описание новости')),
                ('descriptions', models.TextField(blank=True, verbose_name='Подробное описание новости')),
                ('date_create', models.DateField(auto_now_add=True)),
                ('pub', models.BooleanField(verbose_name='Публикация')),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='Картинка новости')),
                ('slug', models.SlugField(blank=True, max_length=200, verbose_name='Ссылка на новость')),
                ('meta_title', models.CharField(blank=True, max_length=150, verbose_name='META TITLE')),
                ('meta_keywords', models.CharField(blank=True, max_length=150, verbose_name='META KEYWORDS')),
                ('meta_descriptions', models.CharField(blank=True, max_length=150, verbose_name='META DESCRIPTIONS')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.AlterIndexTogether(
            name='sale',
            index_together={('id', 'slug')},
        ),
        migrations.AlterIndexTogether(
            name='news',
            index_together={('id', 'slug')},
        ),
    ]
