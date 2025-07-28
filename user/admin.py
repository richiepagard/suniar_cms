from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from user.models import User


class UserAdmin(BaseUserAdmin):
    """ Define Admin page for users. """
    ordering = ['id']
    list_display = ['email', 'first_name', 'last_name', 'is_staff', 'is_superuser']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('اطلاعات شخصی', {'fields': ('first_name', 'last_name', 'mobile')}),
        ('دسترسی ها', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('زمان ها', {'fields': ('last_login',)})

    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser')
        }),
    )

    search_fields = ('email',)

    filter_horizontal = ('groups', 'user_permissions')


admin.site.register(User, UserAdmin)
