# Generated by Django 2.2.6 on 2019-12-18 04:34

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0005_aboutme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='about',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='projects',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]
