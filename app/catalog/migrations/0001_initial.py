# Generated by Django 2.0 on 2019-07-18 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, verbose_name='Атрибут')),
            ],
        ),
        migrations.CreateModel(
            name='AtributeProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atr', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Atr', verbose_name='Свойство')),
            ],
        ),
        migrations.CreateModel(
            name='Atrvalue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, verbose_name='Значение атрибута')),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('meta_title', models.CharField(blank=True, max_length=150, verbose_name='META TITLE')),
                ('meta_keywords', models.CharField(blank=True, max_length=150, verbose_name='META KEYWORDS')),
                ('meta_descriptions', models.CharField(blank=True, max_length=150, verbose_name='META DESCRIPTIONS')),
            ],
            options={
                'verbose_name': 'Бренд',
                'verbose_name_plural': 'Бренды',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55, verbose_name='Категория')),
                ('slug', models.SlugField(blank=True, max_length=200, verbose_name='Ссылка')),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='Изображение')),
                ('descriptions', models.TextField(blank=True, verbose_name='Описание')),
                ('meta_title', models.CharField(blank=True, max_length=150, verbose_name='META TITLE')),
                ('meta_keywords', models.CharField(blank=True, max_length=150, verbose_name='META KEYWORDS')),
                ('meta_descriptions', models.CharField(blank=True, max_length=150, verbose_name='META DESCRIPTIONS')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='catalog.Category', verbose_name='Родительская категория')),
            ],
            options={
                'verbose_name': 'Категории',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование')),
                ('search_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Поисковое имя')),
                ('articul', models.CharField(blank=True, max_length=150, verbose_name='Артикул')),
                ('descriptions', models.TextField(blank=True, verbose_name='Описание')),
                ('date_create', models.DateField(auto_now_add=True)),
                ('sold', models.BooleanField(verbose_name='Продан')),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='Изображение(если нет характеристики)')),
                ('slug', models.SlugField(blank=True, max_length=200, verbose_name='Ссылка на товар')),
                ('hit', models.BooleanField(default=False, verbose_name='Хит')),
                ('new', models.BooleanField(default=False, verbose_name='Новинка')),
                ('sale', models.BooleanField(default=False, verbose_name='Распродажа')),
                ('up', models.BooleanField(default=False, verbose_name='Показывать сверху')),
                ('meta_title', models.CharField(blank=True, max_length=150, verbose_name='META TITLE')),
                ('meta_keywords', models.CharField(blank=True, max_length=150, verbose_name='META KEYWORDS')),
                ('meta_descriptions', models.CharField(blank=True, max_length=150, verbose_name='META DESCRIPTIONS')),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Brand', verbose_name='Бренд')),
                ('category_type', models.ManyToManyField(blank=True, null=True, to='catalog.Category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Товары',
                'verbose_name_plural': 'Товары',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SaleAtr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, verbose_name='Свойство')),
            ],
        ),
        migrations.CreateModel(
            name='SaleAtributeProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='SaleAtrvalue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, verbose_name='Значение свойства')),
            ],
        ),
        migrations.CreateModel(
            name='SaleProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование')),
                ('price', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='Изображение')),
                ('prod', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Предложения',
                'verbose_name_plural': 'Предложение',
            },
        ),
        migrations.AddField(
            model_name='saleatributeproduct',
            name='prod',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.SaleProduct', verbose_name='Предложение'),
        ),
        migrations.AddField(
            model_name='saleatributeproduct',
            name='saleatr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.SaleAtr', verbose_name='Свойство'),
        ),
        migrations.AddField(
            model_name='saleatributeproduct',
            name='saleatrvalue',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.SaleAtrvalue', verbose_name='Значение'),
        ),
        migrations.AddField(
            model_name='atributeproduct',
            name='atrvalue',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Atrvalue', verbose_name='Значение'),
        ),
        migrations.AddField(
            model_name='atributeproduct',
            name='prod',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Product', verbose_name='Товар'),
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together={('id', 'slug')},
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together={('slug', 'parent')},
        ),
    ]
