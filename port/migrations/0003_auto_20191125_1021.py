# Generated by Django 2.2.6 on 2019-11-25 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0002_auto_20191125_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]