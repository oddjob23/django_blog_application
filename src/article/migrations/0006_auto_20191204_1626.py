# Generated by Django 3.0 on 2019-12-04 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_article_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
