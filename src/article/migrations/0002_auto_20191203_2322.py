# Generated by Django 3.0 on 2019-12-03 23:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PostView',
            new_name='ArticleViews',
        ),
    ]
