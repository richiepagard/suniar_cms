from django.contrib import admin

from shop.models import Shop


# Register your models here.
class ShopAdmin(admin.ModelAdmin):
    """ Define admin page for Shop page. """
    ordering = ['id', 'name']
    empty_value_display = '-empty-'
    list_display = ['name', 'owner', 'is_active','work_field']

    fieldsets = [
        (
            None, {'fields': ('name', 'owner')}
        ),
        ('جزئیات', {'fields': ('work_field', 'date_created', 'is_active')})
    ]

    search_fields = ['id', 'name']
    readonly_fields = ['date_created']

    add_fieldsets = (
        (None,
         {
             'classes': ('wide',),
             'fields': ('name', 'owner', 'work_field', 'is_active')
         }),
    )


admin.site.register(Shop, ShopAdmin)
