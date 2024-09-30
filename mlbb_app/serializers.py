from rest_framework import serializers
from mlbb_app.models import mlbb_profile, mlbb_Membership
from mlbb_app.models import mlbb_squad, mlbb_community
from mlbb_app.models import mlbb_Squad_Application
from mlbb_app.models import mlbb_Squad_Invite



class mlbb_profileSerializer(serializers.ModelSerializer):
    class Meta:
        model = mlbb_profile
        fields = ['mlbb_player_id', 'mlbb_player_ign', 'country', 'squad_id', 'Account_id']

class mlbb_squadSerializer(serializers.ModelSerializer):
    class Meta:
        model = mlbb_squad
        fields = '__all__'



class mlbb_Squad_ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = mlbb_Squad_Application
        # fields = ['squad_id', 'squad', 'status']
        fields = '__all__'

class GameSquadInviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = mlbb_Squad_Invite
        # fields = ['squad_id', 'squad', 'user', 'status']
        fields = "__all__"

class Mlbb_MembershipSerializer(serializers.ModelSerializer):
    leader = mlbb_profileSerializer(read_only=True)
    squads = mlbb_squadSerializer(many=True)

    class Meta:
        model = mlbb_Membership
        # fields = ['community_id', 'community_tag', 'community_name', 'community_description',
        #           'community_image', 'leader', 'applicants', 'squads', "community country"]
        fields = '__all__'

class Mlbb_CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = mlbb_community
        fields = '__all__'