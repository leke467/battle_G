from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Account
from django.db import IntegrityError
class AccountSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Account
        fields = ['id', 'first_name', 'username', 'last_name', 'country','email', 'gender', 'age', 'password']
        # fields = "__all__"
        read_only_fields = ['id']

    def validate_email(self, value):
        try:
            user = Account.objects.get(email=value)
            if self.instance:
                if user.pk != self.instance.pk:
                    raise serializers.ValidationError("An account with this email already exists.")
            else:
                if Account.objects.filter(email=value).exists():
                    raise serializers.ValidationError("An account with this email already exists.")
        except Account.DoesNotExist:
            pass
        return value
    def create(self, validated_data):
        try:
            validated_data['password'] = make_password(validated_data['password'])
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError("A Record with this unique field value already exists.")

