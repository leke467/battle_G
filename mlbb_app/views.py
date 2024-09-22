from rest_framework.response import Response
from rest_framework.views import APIView
from squad_app import views as squad_views
from rest_framework import generics, status
from mlbb_app import models
from mlbb_app import serializers
from mlbb_app.serializers import mlbb_profileSerializer
from mlbb_app.models import mlbb_profile
from django.shortcuts import get_object_or_404


class Mlbb_Account_serializer_create(generics.ListCreateAPIView):
    queryset = mlbb_profile.objects.all()
    serializer_class = mlbb_profileSerializer


class mlbb_Account_update(generics.RetrieveUpdateDestroyAPIView):
    queryset = mlbb_profile.objects.all()
    serializer_class = serializers.mlbb_profileSerializer
    lookup_field = 'mlbb_player_id'




class mlbb_squad_create(squad_views.SquadCreateBase):
    queryset = models.mlbb_squad.objects.all()
    serializer_class = serializers.mlbb_squadSerializer
    squad_id_field = "squad_id"

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            user_profile = self.request.user.profile
            serializer.save(leader=user_profile, leader_id=user_profile.mlbb_player_id)
        else:
            return Response("Unauthorized", status=status.HTTP_403_FORBIDDEN)



class mlbbSquadRetrieveUpdateDestroy(squad_views.SquadRetrieveUpdateDestroyBase):
    queryset = models.mlbb_squad.objects.all()
    serializer_class = serializers.mlbb_squadSerializer

class mlbbSquadView(APIView):
    queryset = models.mlbb_squad.objects.all()
    def get(self, request):
        squads = models.mlbb_squad.objects.all()
        serializer = serializers.mlbb_squadSerializer(squads, many=True)
        return Response(serializer.data)


# Import generics at the beginning
from rest_framework import generics


class SendSquadInviteView(generics.CreateAPIView):
    queryset = models.mlbb_Squad_Invite.objects.all()
    serializer_class = serializers.GameSquadInviteSerializer


class UpdateSquadInviteView(generics.UpdateAPIView):
    queryset = models.mlbb_Squad_Invite.objects.all()
    serializer_class = serializers.GameSquadInviteSerializer


class ApplyToSquadView(generics.CreateAPIView):
    queryset = models.mlbb_Squad_Application.objects.all()
    serializer_class = serializers.mlbb_Squad_ApplicationSerializer

    def create(self, request, *args, **kwargs):
        squad = get_object_or_404(models.mlbb_squad, id=kwargs.get("squad_id"))
        player = request.user.mlbb_profile
        application = models.mlbb_Squad_Application(squad=squad, player=player)
        application.save()
        serializer = self.get_serializer(application)
        return Response(serializer.data)


class UpdateSquadApplicationView(generics.UpdateAPIView):
    queryset = models.mlbb_Squad_Application.objects.all()
    serializer_class = serializers.mlbb_Squad_ApplicationSerializer


