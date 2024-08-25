from django.contrib.auth.backends import ModelBackend
from player_Account.models import Account

class Account_Auth_Backend(ModelBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            # Fetch the user by email
            user = Account.objects.get(email=email)
            # Check if the provided password matches the stored hashed password
            if user.check_password(password):
                return user
        except Account.DoesNotExist:
            return None