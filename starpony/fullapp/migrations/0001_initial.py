# Generated by Django 3.0.2 on 2020-01-21 12:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='Автор долбоеб', help_text='Название статьи', max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('text', models.TextField(default='Автор долбоеб', max_length=500)),
                ('fil', models.FileField(null=True, upload_to='documents/')),
                ('date', models.DateField(auto_now=True)),
                ('status', models.CharField(blank=True, choices=[('В теории', 'В теории'), ('В проекте', 'Проектирование'), ('Альфа', 'Альфа'), ('Бета', 'Бета'), ('Релиз', 'Релиз')], default='t', max_length=10)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='Автор долбоеб', help_text='Название статьи', max_length=200)),
                ('image', models.ImageField(default='image not found', upload_to='images')),
                ('text', models.TextField(default='Автор долбоеб', max_length=1000)),
                ('date', models.DateField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
