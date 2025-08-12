from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
	"""
    Custom base user manager to manage users creation such as create superuser.

    Methods:
        create_user: Create a redimentary user with required fields.
        create_superuser: Create a superuser to set full access on admin panel with required fields.
    """
	def create_user(
		self, phone_number: str, username: str,
		email: str=None, first_name: str=None, last_name: str=None,
		password=None
	):
		"""
        Create a redimentary user with required fields,
        Check if user has phone number and username to verify them.

        Arguments:
            phone_number (str): User phone number, user will verify by it.
            username (str): A unique identifier for authentication, display name shown in the user interface.
            email (str): User email address, user will verify by it, too.
            first_name (str): Optional user first name.
            last_name (str): Optional user last name.
            password (str): Could be None because user could register with OTP code.
        """
		if not phone_number:
			raise ValueError(_("User must has a phone number to identify."))
		if not username:
			raise ValueError(_("User must has a username for recognization."))

		user = self.model(
			phone_number=phone_number,
			username=username,
			# Normalize email to prevent inconsistencies that could lead to `unkind` attacks,
			# where different variations of an email might bypass security checks.
			email=self.normalize_email(email),
			first_name=first_name,
			last_name=last_name
		)

		user.set_password(password)
		user.save(using=self._db)

		return user

	def create_superuser(
		self, phone_number: str, username: str,
		email: str=None, first_name: str=None, last_name: str=None,
		password=None
	):
		"""
        Create a superuser with reuired fields and activation status of Is Superuser.
        Check if the Is Staff and Is Superuser status are active for created superuser.

        Arguments:
            phone_number (str): User phone number, user will verify by it.
            username (str): A unique identifier for authentication, display name shown in the user interface.
            email (str): User email address, user will verify by it, too.
            first_name (str): Optional user first name.
            last_name (str): Optional user last name.
            password (str): Could be None because user could register with OTP code or by 'createsuperuser' command.
        """
		user = self.create_user(
			phone_number=phone_number,
			username=username,
			email=email,
			first_name=first_name,
			last_name=last_name,
			password=password
		)

		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)

		return user
