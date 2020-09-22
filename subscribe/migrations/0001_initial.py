# Generated by Django 3.1.1 on 2020-09-20 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('frequency', models.CharField(max_length=254)),
                ('paid', models.CharField(max_length=254)),
                ('incentive1', models.CharField(blank=True, max_length=254, null=True)),
                ('incentive2', models.CharField(blank=True, max_length=254, null=True)),
                ('incentive3', models.CharField(blank=True, max_length=254, null=True)),
                ('incentive4', models.CharField(blank=True, max_length=254, null=True)),
                ('incentive5', models.CharField(blank=True, max_length=254, null=True)),
                ('incentive6', models.CharField(blank=True, max_length=254, null=True)),
                ('incentive7', models.CharField(blank=True, max_length=254, null=True)),
                ('incentive8', models.CharField(blank=True, max_length=254, null=True)),
                ('incentive9', models.CharField(blank=True, max_length=254, null=True)),
                ('incentive10', models.CharField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]