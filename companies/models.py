from django.db import models


class Role(models.IntegerChoices):
    """
    Описывает набор возможных значений для поля 'role' класса 'Company'
    """
    plant = 1, 'Завод'
    retail = 2, 'Розничная сеть'
    trader = 3, 'Индивидуальный предприниматель'


class Company(models.Model):
    """Модель участника торговой сети"""

    class Meta:
        verbose_name = 'Участник торговой сети'
        verbose_name_plural = 'Участники торговой сети'

    def __str__(self):
        return self.title

    title = models.CharField(verbose_name='Название', max_length=255)
    role = models.PositiveSmallIntegerField(
        verbose_name='Роль в торговой сети', choices=Role.choices, default=Role.trader
    )
    email = models.EmailField(verbose_name='E-mail')
    country = models.CharField(verbose_name='Страна', max_length=64)
    town = models.CharField(verbose_name='Город', max_length=64)
    street = models.CharField(verbose_name='Улица', max_length=64)
    house = models.PositiveSmallIntegerField(verbose_name='Дом')
    created = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    supplier = models.ForeignKey(
        'self', verbose_name='Поставщик', null=True, blank=True, on_delete=models.PROTECT)
    debt = models.FloatField(verbose_name='Задолженность перед поставщиком')


class Product(models.Model):
    """Модель продукта в торговой сети"""

    class Meta:
        verbose_name = 'Продукт торговой сети'
        verbose_name_plural = 'Продукты торговой сети'

    def __str__(self):
        return self.title

    title = models.CharField(verbose_name='Название', max_length=255)
    model = models.CharField(verbose_name='Модель', max_length=255)
    release_date = models.DateField(verbose_name='Дата выхода продукта на рынок')

    # У участника торговой сети может быть множество продуктов
    # Одна и та же модель продукта может быть представлена у разных участников торговой сети
    companies = models.ManyToManyField(Company)
