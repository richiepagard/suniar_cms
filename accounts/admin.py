from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from shop.models import Shop
from accounts.models import User


class MemberShipInLine(admin.TabularInline):
    model = Shop.members.through
    extra = 1


class UserAdmin(BaseUserAdmin):
    list_display = ['phone_number', 'username', 'is_superuser', 'role']
    search_fields = ('phone_number', 'username', 'email',)
    readonly_fields = ['last_login']
    inlines = [
        MemberShipInLine
    ]

    fieldsets = (
        (_('Authorize Info'), {'fields': ('phone_number', 'username', 'email', 'password')}),
        (_('Personal Info'), {'fields': ('first_name', 'last_name', 'role')}),
        (_('Permissions'), {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Date Times'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (_("Add New User"), {
            'classes': ('wide',),
            'fields': (
                'phone_number', 'username', 'email', 'password', 'password2', 'is_active',
                'is_staff', 'is_superuser', 'role'
            )
        }),
    )

    filter_horizontal = ('groups', 'user_permissions')


admin.site.register(User, UserAdmin)
