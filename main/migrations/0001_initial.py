# Generated by Django 4.0.2 on 2022-02-27 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Дата')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество')),
                ('distance', models.PositiveIntegerField(verbose_name='Расстояние')),
            ],
            options={
                'verbose_name': 'Таблица',
                'verbose_name_plural': 'Таблицы',
            },
        ),
    ]