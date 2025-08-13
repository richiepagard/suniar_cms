from django.urls import path

from accounts.views import UserLoginView

app_name = 'accounts'

USER_AUTHENTICATION_URLS = [
    path("users/login/", UserLoginView.as_view(), name="user-login"),
]

urlpatterns = USER_AUTHENTICATION_URLS
