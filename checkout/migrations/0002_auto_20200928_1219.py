# Generated by Django 3.1.1 on 2020-09-28 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='original_cart',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='order',
            name='stripe_payment_id',
            field=models.CharField(default='', max_length=254),
        ),
    ]
