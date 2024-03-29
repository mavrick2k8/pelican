# Generated by Django 2.0 on 2019-07-26 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_new_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='apartment',
        ),
        migrations.RemoveField(
            model_name='order',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='order',
            name='house',
        ),
        migrations.RemoveField(
            model_name='order',
            name='postal_code',
        ),
        migrations.RemoveField(
            model_name='order',
            name='street',
        ),
        migrations.AddField(
            model_name='order',
            name='comment',
            field=models.TextField(blank=True, verbose_name='Комментарий'),
        ),
        migrations.AddField(
            model_name='order',
            name='order_delivery',
            field=models.IntegerField(blank=True, null=True, verbose_name='Доставка'),
        ),
        migrations.AddField(
            model_name='order',
            name='order_payment',
            field=models.IntegerField(blank=True, null=True, verbose_name='Оплата'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='atributeproduct_name',
            field=models.CharField(blank=True, max_length=300, verbose_name='Наименование'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product_name',
            field=models.CharField(blank=True, max_length=300, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='atributeproduct',
            field=models.IntegerField(blank=True, null=True, verbose_name='Характеристика товара'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.IntegerField(blank=True, null=True, verbose_name='Характеристика товара'),
        ),
    ]
