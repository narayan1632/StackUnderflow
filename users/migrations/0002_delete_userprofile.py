# Generated by Django 4.1.4 on 2022-12-13 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_newsmodel_author'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
