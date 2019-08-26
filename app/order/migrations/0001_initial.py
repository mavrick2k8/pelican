# Generated by Django 2.0 on 2019-07-18 10:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_new', models.CharField(choices=[('Новый', 'Новый'), ('Отправлен', 'Отправлен'), ('Получен', 'Поучен'), ('Отменен', 'Отменен')], default='Новый', max_length=10, verbose_name='Статус')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Обновлен')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('trackid', models.CharField(blank=True, max_length=150, null=True, verbose_name='Номер отслеживания')),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryMetod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('attr', models.CharField(max_length=50, verbose_name='Атрибут 1')),
                ('attrmetod', models.CharField(max_length=50, verbose_name='Атрибут 2')),
            ],
            options={
                'verbose_name_plural': 'Варианты доставки',
                'verbose_name': 'Доставка',
            },
        ),
        migrations.CreateModel(
            name='Oplata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid', models.BooleanField(default=False, verbose_name='Оплачен')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Обновлен')),
                ('payment_id', models.CharField(blank=True, max_length=720, null=True, verbose_name='ИД Кассы')),
                ('status_new', models.CharField(choices=[('Новый', 'Новый'), ('Оплачен', 'Оплачен'), ('Возврат', 'Возврат'), ('Отменен', 'Отменен')], default='Новый', max_length=10, verbose_name='Статус оплаты')),
            ],
            options={
                'verbose_name_plural': 'Оплаты',
                'verbose_name': 'Оплата',
            },
        ),
        migrations.CreateModel(
            name='OplataMetod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('attr', models.CharField(max_length=50, verbose_name='Атрибут 1')),
            ],
            options={
                'verbose_name_plural': 'Варианты оплаты',
                'verbose_name': 'Оплата',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, verbose_name='ФИО')),
                ('last_name', models.CharField(blank=True, max_length=50, verbose_name='Доп. поле')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('address', models.CharField(max_length=250, verbose_name='Город ')),
                ('postal_code', models.CharField(max_length=20, verbose_name='Почтовый код')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('paid', models.BooleanField(default=False, verbose_name='Оплачен')),
                ('street', models.CharField(blank=True, max_length=150, verbose_name='Улица')),
                ('house', models.CharField(blank=True, max_length=150, verbose_name='Дом')),
                ('apartment', models.CharField(blank=True, max_length=150, verbose_name='Квартира')),
                ('numbers', models.CharField(blank=True, max_length=250, verbose_name='Номер телефона')),
                ('discount', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Скидка')),
            ],
            options={
                'ordering': ('-created',),
                'verbose_name_plural': 'Заказы',
                'verbose_name': 'Заказ',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Количество')),
                ('atributeproduct', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.AtributeProduct', verbose_name='Характеристика товара')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='order.Order', verbose_name='Заказ')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_items', to='catalog.Product', verbose_name='Товар')),
            ],
        ),
        migrations.AddField(
            model_name='oplata',
            name='name_new',
            field=models.ForeignKey(blank=True, null=True, on_delete='', to='order.OplataMetod', verbose_name='Способ оплаты'),
        ),
        migrations.AddField(
            model_name='oplata',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.Order', verbose_name='Заказ'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='dostavka',
            field=models.ForeignKey(blank=True, null=True, on_delete='', to='order.DeliveryMetod', verbose_name='Способ доставки'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.Order', verbose_name='Заказ'),
        ),
    ]
