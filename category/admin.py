from django.contrib import admin

from category.models import Category


class CategoryAdmin(admin.ModelAdmin):
    """ Customize admin page for category model. """
    ordering = ['id']
    empty_value_display = '-empty-'
    list_display = ['name', 'description', 'is_active']
    fieldsets = [
        (
            None, {'fields': ('name',)}
        ),
        (
            'جزئیات', {'fields': ('description', 'is_active')}
        )
    ]

    add_fieldset = (
        (None, {
            'class': ('wide',),
            'fields': ('name', 'description', 'is_active')
        }),
    )


admin.site.register(Category, CategoryAdmin)
