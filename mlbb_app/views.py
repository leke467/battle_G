from rest_framework.response import Response
from rest_framework.views import APIView
from squad_app import views as squad_views
from rest_framework import generics
from mlbb_app import models
from mlbb_app import serializers
from mlbb_app.serializers import mlbb_profileSerializer
from mlbb_app.models import mlbb_profile


class Mlbb_Account_serializer_create(generics.ListCreateAPIView):
    queryset = mlbb_profile.objects.all()
    serializer_class = mlbb_profileSerializer

class mlbb_squad_create(squad_views.SquadCreateBase):
    queryset = models.mlbb_squad.objects.all()
    serializer_class = serializers.mlbb_squadSerializer
    squad_id_field = "squad_id"

    def perform_create(self, serializer):
        user_profile = self.request.user.profile
        serializer.save(leader=user_profile, leader_id=user_profile.mlbb_id)




class mlbbSquadRetrieveUpdateDestroy(squad_views.SquadRetrieveUpdateDestroyBase):
    queryset = models.mlbb_squad.objects.all()
    serializer_class = serializers.mlbb_squadSerializer

class mlbbSquadView(APIView):
    def get(self, request):
        squads = models.mlbb_squad.objects.all()
        serializer = serializers.mlbb_squadSerializer(squads, many=True)
        return Response(serializer.data)


class SendSquadInviteView(APIView):
    def post(self, request, squad_id, player_id):
        squad = models.mlbb_squad.objects.get(id=squad_id)
        player = models.mlbb_profile.objects.get(id=player_id)
        invite = models.mlbb_Squad_Invite(squad=squad, player=player)
        invite.save()
        serializer = serializers.GameSquadInviteSerializer(invite)
        return Response(serializer.data)


class UpdateSquadInviteView(APIView):
    def patch(self, request, invite_id):
        invite = models.mlbb_Squad_Invite.objects.get(id=invite_id)
        serializer = serializers.GameSquadInviteSerializer(invite, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class ApplyToSquadView(APIView):
    def post(self, request, squad_id):
        squad = models.mlbb_squad.objects.get(id=squad_id)
        player = request.user.mlbb_profile
        application = models.mlbb_Squad_Application(squad=squad, player=player)
        application.save()
        serializer = serializers.mlbb_Squad_ApplicationSerializer(application)
        return Response(serializer.data)

class UpdateSquadApplicationView(APIView):
    def patch(self, request, application_id):
        application = models.mlbb_Squad_Application.objects.get(id=application_id)
        serializer = serializers.mlbb_Squad_ApplicationSerializer(application, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

