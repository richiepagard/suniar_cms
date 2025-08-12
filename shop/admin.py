from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from shop.models import Shop


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'is_active', 'work_field']
    search_fields = ['id', 'name']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['id', 'name']
    empty_value_display = '-empty-'

    fieldsets = [
        (
            _('Base Info'), {'fields': ('name', 'owner')}
        ),
        (_('Detail'), {
            'fields': ('work_field', 'date_created', 'is_active', 'members', 'category')
            }
        )
    ]

    add_fieldsets = (
        (_('Add new shop'),
         {
             'classes': ('wide',),
             'fields': ('name', 'owner', 'work_field', 'is_active', 'members', 'category')
         }),
    )
