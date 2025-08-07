# from django.contrib.auth.models import ContentType
# from django.contrib.auth.models import Permission
#
# from shop.models import Shop
# from user.groups import *
#
# content_type = ContentType.objects.get_for_model(Shop)
# read_permission = Permission.objects.create(
#     content_type=content_type,
#     codename='can_just_view_shop',
#     name='Can Just View Shop List',
# )
#
# content_type = ContentType.objects.get_for_model(Shop)
# publish_permission = Permission.objects.create(
#     content_type=content_type,
#     codename='can_publish_shop',
#     name='Can View and Publish Shop',
# )
#
# content_type = ContentType.objects.get_for_model(Shop)
# full_access_permission = Permission.objects.create(
#     content_type=content_type,
#     codename='full_access_shop',
#     name='Can do anything to shop_FullAccess',
# )
#
# group_user.permissions.add(read_permission)
# group_programmer.permissions.add(publish_permission)
# group_ceo.permissions.add(full_access_permission)
