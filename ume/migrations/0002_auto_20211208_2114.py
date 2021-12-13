# Generated by Django 3.1.7 on 2021-12-08 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20211208_2050'),
        ('ume', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerpost',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.seller', verbose_name='custom user'),
        ),
    ]
