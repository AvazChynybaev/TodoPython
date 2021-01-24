# Generated by Django 3.1.4 on 2021-01-24 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=1000)),
                ('price', models.IntegerField()),
                ('genre', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]