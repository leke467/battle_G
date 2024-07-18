
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from player_Account.models import Account
from player_Account.serializers import AccountSerializer
from player_Account.backends import Account_Auth_Backend

class AccountListCreate(generics.ListCreateAPIView):
    authentication_classes = [Account_Auth_Backend]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        if Account.objects.filter(email=email).exists():
            return Response({'error': 'Email address already in use'}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)

class AccountRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [Account_Auth_Backend]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_field = 'pk'

    def delete(self, request, *args, **kwargs):
        pk = kwargs['pk']
        account = Account.objects.get(pk=pk)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        print(email, password)
        user = Account_Auth_Backend().authenticate(request, email, password)
        print(user)
        if user:
            serializer = AccountSerializer(user)
            data = serializer.data
            return Response({'message': 'Login successful', 'user': data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)

