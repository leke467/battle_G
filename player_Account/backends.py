
from django.contrib.auth.backends import ModelBackend
from player_Account.models import Account

class Account_Auth_Backend(ModelBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            user = Account.objects.get(email=email)
            print("aut", user.password)
            print("pas", password)
            print("aut", user.check_password(password))
            if user.password == password:
                return user
        except Account.DoesNotExist:
            return None
