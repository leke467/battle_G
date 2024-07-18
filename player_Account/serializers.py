
from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = Account
        fields = ['id', 'first_name', 'last_name', 'country', 'gender', 'email', "age", 'password']
