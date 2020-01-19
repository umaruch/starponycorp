# Generated by Django 3.0.2 on 2020-01-16 08:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.CharField(default='Автор долбоеб', help_text='Название статьи', max_length=200)),
                ('text', models.TextField(default='Автор долбоеб', max_length=500)),
                ('file_ref', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now=True)),
                ('status', models.CharField(blank=True, choices=[('t', 'В теории'), ('p', 'Проектирование'), ('a', 'Альфа'), ('b', 'Бета'), ('r', 'Релиз')], default='t', max_length=1)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
