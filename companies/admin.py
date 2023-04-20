from django.contrib import admin

from .models import Company, Product


# Регистрируем модели с собственными панелями администратора
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """Модель участника торговой сети"""
    list_display = ['title', 'role']
    list_filter = ['town']
    search_fields = ['title']
    search_help_text = 'Поиск по названию участника торговой сети'
    actions = ['clear_debt']

    @admin.action(description='Очистить задолженность перед поставщиком')
    def clear_debt(self, request, queryset):
        queryset.update(debt=0)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Модель продукта торговой сети"""
    list_display = ['title', 'model']
    list_filter = ['model']
    search_fields = ['title']
    search_help_text = 'Поиск по названию продукта торговой сети'
