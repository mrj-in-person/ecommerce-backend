# Generated by Django 4.2.7 on 2023-11-23 11:26

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='carts',
            unique_together={('id', 'created_by')},
        ),
    ]
