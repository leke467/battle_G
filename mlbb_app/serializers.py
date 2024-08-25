from rest_framework import serializers
from mlbb_app.models import mlbb_profile
from mlbb_app.models import mlbb_squad
from mlbb_app.models import mlbb_Squad_Application
from mlbb_app.models import mlbb_Squad_Invite



class mlbb_profileSerializer(serializers.ModelSerializer):
    class Meta:
        model = mlbb_profile
        fields = ['mlbb_player_id', 'mlbb_player_ign', 'country', 'squad_id']

class mlbb_squadSerializer(serializers.ModelSerializer):
    class Meta:
        model = mlbb_squad
        fields = '__all__'



class mlbb_Squad_ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = mlbb_Squad_Application
        fields = ['id', 'squad', 'player', 'status']

class GameSquadInviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = mlbb_Squad_Invite
        fields = ['id', 'squad', 'player', 'status']
