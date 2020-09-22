# Generated by Django 3.1.1 on 2020-09-21 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(max_length=254)),
                ('discipline1', models.CharField(max_length=254)),
                ('discipline2', models.CharField(blank=True, max_length=254, null=True)),
                ('description', models.TextField()),
                ('skill_level1', models.CharField(max_length=254)),
                ('skill_level2', models.CharField(blank=True, max_length=254, null=True)),
                ('skill_level3', models.CharField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MasterclassOverview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('masterclass_title', models.CharField(max_length=254)),
                ('artist_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lessons.artist')),
            ],
        ),
        migrations.CreateModel(
            name='Masterclass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_title', models.CharField(max_length=254)),
                ('lesson_description', models.TextField()),
                ('video_url', models.URLField(max_length=1024)),
                ('masterclass_title', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lessons.masterclassoverview')),
            ],
        ),
    ]