# Generated by Django 3.0.2 on 2020-01-17 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20200117_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='image not found', upload_to='images'),
        ),
    ]
