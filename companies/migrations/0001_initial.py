# Generated by Django 4.2 on 2023-04-19 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('role', models.PositiveSmallIntegerField(choices=[(1, 'Завод'), (2, 'Розничная сеть'), (3, 'Индивидуальный предприниматель')], default=3, verbose_name='Роль в торговой сети')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('country', models.CharField(max_length=64, verbose_name='Страна')),
                ('town', models.CharField(max_length=64, verbose_name='Город')),
                ('street', models.CharField(max_length=64, verbose_name='Улица')),
                ('house', models.PositiveSmallIntegerField(verbose_name='Дом')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('debt', models.FloatField(verbose_name='Задолженность перед поставщиком')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='companies.company', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Участник торговой сети',
                'verbose_name_plural': 'Участники торговой сети',
            },
        ),
    ]