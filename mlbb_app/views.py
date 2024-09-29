from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework import generics, status
from mlbb_app import models
from mlbb_app import serializers
from mlbb_app.serializers import mlbb_profileSerializer

from django.shortcuts import get_object_or_404


class Mlbb_Account_serializer_create(generics.ListCreateAPIView):
    queryset = models.mlbb_profile.objects.all()
    serializer_class = mlbb_profileSerializer



class mlbb_Account_update(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.mlbb_profile.objects.all()
    serializer_class = serializers.mlbb_profileSerializer
    lookup_field = 'mlbb_player_id'

class mlbbSquadCreate(generics.ListCreateAPIView):
    queryset = models.mlbb_squad.objects.all()
    serializer_class = serializers.mlbb_squadSerializer
    squad_id_field = "squad_id"

class mlbbSquadRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.mlbb_squad.objects.all()
    serializer_class = serializers.mlbb_squadSerializer
    lookup_field = "pk"

    def delete(self, request, *args, **kwargs):
        pk = kwargs['pk']
        squad = self.get_object().get(pk=pk)
        squad.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class mlbbSquadView(generics.ListAPIView):
    serializer_class = serializers.mlbb_squadSerializer

    def get_queryset(self):
        try:
            return models.mlbb_squad.objects.all()
        except ObjectDoesNotExist:
            return Response({"error": "mlbb_squad not found"}, status=status.HTTP_404_NOT_FOUND)


class SendSquadInviteView(generics.ListAPIView):
    queryset = models.mlbb_Squad_Invite.objects.all()
    serializer_class = serializers.GameSquadInviteSerializer


class UpdateSquadInviteView(generics.UpdateAPIView):
    queryset = models.mlbb_Squad_Invite.objects.all()
    serializer_class = serializers.GameSquadInviteSerializer


class ApplyToSquadView(generics.ListCreateAPIView):
    queryset = models.mlbb_Squad_Application.objects.all()
    serializer_class = serializers.mlbb_Squad_ApplicationSerializer


class UpdateSquadApplicationView(generics.UpdateAPIView):
    queryset = models.mlbb_Squad_Application.objects.all()
    serializer_class = serializers.mlbb_Squad_ApplicationSerializer


