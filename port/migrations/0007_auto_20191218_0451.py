# Generated by Django 2.2.6 on 2019-12-18 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0006_auto_20191218_0434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='about',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='projects',
            name='description',
            field=models.TextField(),
        ),
    ]
