# Generated by Django 3.0.1 on 2020-01-11 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0008_aboutme_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='image',
            field=models.ImageField(upload_to='static/'),
        ),
        migrations.AlterField(
            model_name='backgroundimage',
            name='bg_image',
            field=models.ImageField(upload_to='static/'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.ImageField(upload_to='static/'),
        ),
    ]