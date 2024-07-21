from django.contrib import admin
from .models import Type, Valyuta, Balance, Income, Outcome


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['type_name', 'type_icon']
    search_fields = ['type_name']


@admin.register(Valyuta)
class ValyutaAdmin(admin.ModelAdmin):
    list_display = ['name_valyuta', 'price_per_dollar', 'icon']
    search_fields = ['name_valyuta']


@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    list_display = ['user', 'value', 'type', 'date', 'comment', 'valyuta', 'created_at', 'updated_at']
    search_fields = ['user__username', 'type__type_name', 'valyuta__name_valyuta']
    list_filter = ['date', 'type', 'valyuta']


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ['user', 'value', 'type', 'date', 'comment', 'valyuta', 'created_at', 'updated_at']
    search_fields = ['user__username', 'type__type_name', 'valyuta__name_valyuta']
    list_filter = ['date', 'type', 'valyuta']


@admin.register(Outcome)
class OutcomeAdmin(admin.ModelAdmin):
    list_display = ['user', 'value', 'type', 'date', 'comment', 'valyuta', 'created_at', 'updated_at']
    search_fields = ['user__username', 'type__type_name', 'valyuta__name_valyuta']
    list_filter = ['date', 'type', 'valyuta']
