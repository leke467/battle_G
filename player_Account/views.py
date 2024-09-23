from rest_framework.views import APIView

from rest_framework import generics, status
from rest_framework.response import Response
from django.db import IntegrityError, transaction
from player_Account.models import Account
from player_Account.serializers import AccountSerializer
from player_Account.backends import Account_Auth_Backend
import logging
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.authtoken.models import Token


class AccountListCreate(generics.ListCreateAPIView):
    authentication_classes = [Account_Auth_Backend]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        if email is not None:
            email = email.strip().lower()
        else:
            return Response({'error': 'Email field is required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            # Check if the email already exists in a non-atomic block
            if Account.objects.filter(email=email).exists():
                return Response({'error': 'Email address already in use'}, status=status.HTTP_400_BAD_REQUEST)

            # Proceed with creation inside an atomic block
            with transaction.atomic():
                return super().create(request, *args, **kwargs)

        except IntegrityError as e:
            error_message = str(e)
            print(f"IntegrityError: {error_message}")  # Log the full error message for debugging

            if 'UNIQUE constraint' in error_message or 'duplicate key' in error_message:
                return Response({'error': 'Duplicate entry detected. The email already exists.'},
                                status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': f'An error occurred: {error_message}'},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AccountRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [Account_Auth_Backend]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_field = 'pk'

    def delete(self, request, *args, **kwargs):
        pk = kwargs['pk']
        try:
            account = Account.objects.get(pk=pk)
            account.is_active = False  # Updating status instead of deleting
            account.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Account.DoesNotExist:
            return Response({"error": "Account not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:  # Catch-all exception handler
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


logger = logging.getLogger(__name__)



class LoginView(APIView):
    account_auth_backend = Account_Auth_Backend()  # Only one instance

    def post(self, request):
        email = self.normalize_email(request.data.get('email'))
        password = request.data.get('password')

        # Hash the provided password
        hashed_password = make_password(password)

        # Don't log sensitive information such as email and hashed passwords
        logger.debug("Login attempt made")

        # Use check_password to compare provided password with stored hashed password
        account = self.account_auth_backend.authenticate(request, email, hashed_password)

        logger.debug(f"Authenticated user: {account}")
        if account is not None:
            token, _ = Token.objects.get_or_create(user=account)

            # Ensure that the token is unique
            if token.user != account:
                token.delete()
                token = Token.objects.create(user=account)

            serializer = AccountSerializer(account)
            data = serializer.data
            return Response({'message': 'Login successful', 'user': data, 'token': token.key},
                            status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)

    def normalize_email(self, email):
        normalized_email = email.strip().lower()
        local, _, domain = normalized_email.partition('@')
        local = local.replace('.', '')
        return '{}@{}'.format(local, domain)


