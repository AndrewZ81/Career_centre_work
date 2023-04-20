# Generated by Django 4.2 on 2023-04-20 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('model', models.CharField(max_length=255, verbose_name='Модель')),
                ('release_date', models.DateField(verbose_name='Дата выхода продукта на рынок')),
                ('companies', models.ManyToManyField(to='companies.company')),
            ],
            options={
                'verbose_name': 'Продукт торговой сети',
                'verbose_name_plural': 'Продукты торговой сети',
            },
        ),
    ]