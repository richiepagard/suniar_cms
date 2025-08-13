from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from phonenumber_field.serializerfields import PhoneNumberField

from accounts.utils.jwt_token_generator import get_tokens_for_user


class UserLoginSerializer(serializers.Serializer):
    """
    User login serialization. Validate user and authenticate it.
    """
    phone_number = PhoneNumberField(region="IR")
    password = serializers.CharField(write_only=True)

    default_error_messages = {
        'missing_fields': _('Both phone number and password are required.'),
        'invalid_credentials': _('Invalid login credentials.'),
        'inactive_account': _('User account is disabled.')
    }

    def validate(self, attrs: dict) -> dict:
        """
        Authenticate and validate user.
        Validation for phone number and password fields.

        Returns:
            ValidationError if phone number or password is empty.
            ValidationError if authenticated user is None.
            ValidationError if user does not an active user.
            dict if the data validated successfully and user authenticated,
                it contains user data.
        """
        phone_number = attrs.get("phone_number")
        password = attrs.get("password")

        if not phone_number or not password:
            raise serializers.ValidationError(_(self.error_messages["missing_fields"]))
        
        # Authenticate user
        user = authenticate(
            request=self.context.get("request"),
            phone_number=phone_number,
            password=password
        )

        if not user:
            raise serializers.ValidationError(_(self.error_messages["invalid_credentials"]))

        if not user.is_active:
            raise serializers.ValidationError(_(self.error_messages["inactive_account"]))

        # Store user to using it in 'save' method
        self.user = user
        self.tokens = get_tokens_for_user(self.user)
        # Updates 'attrs' to store user info
        attrs["user"] = user
        return attrs

    def get_response_data(self, *args, **kwargs):
        """
        Calling it after 'is_valid()' method in views
        to done the user login process.

        Returns user information include user tokens for authentication.
        """
        user_info = {
            "user_id": self.user.pk,
            "phone_number": str(self.user.phone_number),
            "tokens": self.tokens
        }

        return user_info
