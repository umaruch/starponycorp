# Generated by Django 3.0.2 on 2020-01-17 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20200117_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(blank=True, choices=[('В теории', 'В теории'), ('В проекте', 'Проектирование'), ('Альфа', 'Альфа'), ('Бета', 'Бета'), ('Релиз', 'Релиз')], default='t', max_length=10),
        ),
    ]
