# Generated by Django 2.0 on 2019-07-31 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_auto_20190728_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oplata',
            name='status_new',
            field=models.CharField(choices=[('NEW', 'Новый'), ('PAID', 'Оплачен'), ('RESEND', 'Возврат'), ('CANCEL', 'Отменен')], max_length=10, verbose_name='Статус оплаты'),
        ),
    ]