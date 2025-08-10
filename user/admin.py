from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from shop.models import Shop
from user.models import User


class MemberShipInLine(admin.TabularInline):
    model = Shop.members.through
    extra = 1


class UserAdmin(BaseUserAdmin):
    """ Define Admin page for users. """
    ordering = ['id']
    list_display = ['email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'role']
    inlines = [
        MemberShipInLine
    ]

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('اطلاعات شخصی', {'fields': ('first_name', 'last_name', 'mobile', 'role')}),
        ('دسترسی ها', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('زمان ها', {'fields': ('last_login',)})

    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser', 'role')
        }),
    )

    search_fields = ('email',)

    filter_horizontal = ('groups', 'user_permissions')


admin.site.register(User, UserAdmin)
