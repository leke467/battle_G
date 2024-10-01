from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework import generics, status
from mlbb_app import models
from mlbb_app import serializers
from mlbb_app.serializers import mlbb_profile_serializer

from django.shortcuts import get_object_or_404


class Mlbb_Account_serializer_create(generics.ListCreateAPIView):
    queryset = models.mlbb_profile.objects.all()
    serializer_class = mlbb_profile_serializer



class mlbb_Account_update(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.mlbb_profile.objects.all()
    serializer_class = serializers.mlbb_profile_serializer
    lookup_field = 'mlbb_player_id'

class Mlbb_squad_create(generics.ListCreateAPIView):
    queryset = models.mlbb_squad.objects.all()
    serializer_class = serializers.mlbb_squad_serializer
    squad_id_field = "squad_id"

class mlbb_squad_retrieve_update_destroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.mlbb_squad.objects.all()
    serializer_class = serializers.mlbb_squad_serializer
    lookup_field = "pk"

    def delete(self, request, *args, **kwargs):
        pk = kwargs['pk']
        squad = self.get_object().get(pk=pk)
        squad.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class mlbb_squad_view(generics.ListAPIView):
    serializer_class = serializers.mlbb_squad_serializer

    def get_queryset(self):
        try:
            return models.mlbb_squad.objects.all()
        except ObjectDoesNotExist:
            return Response({"error": "mlbb_squad not found"}, status=status.HTTP_404_NOT_FOUND)


class Send_squad_invite_view(generics.ListAPIView):
    queryset = models.mlbb_Squad_Invite.objects.all()
    serializer_class = serializers.Game_squad_invite_serializer


class Update_squad_invite_view(generics.UpdateAPIView):
    queryset = models.mlbb_Squad_Invite.objects.all()
    serializer_class = serializers.Game_squad_invite_serializer


class Apply_to_squad_view(generics.ListCreateAPIView):
    queryset = models.mlbb_Squad_Application.objects.all()
    serializer_class = serializers.mlbb_Squad_Application_serializer


class Update_squad_application_view(generics.UpdateAPIView):
    queryset = models.mlbb_Squad_Application.objects.all()
    serializer_class = serializers.mlbb_Squad_Application_serializer

class Create_mlbb_community_view(generics.ListCreateAPIView):
    queryset = models.mlbb_community.objects.all()
    serializer_class = serializers.Mlbb_community_serializer

class Update_mlbb_community_view(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.mlbb_community.objects.all()
    serializer_class = serializers.Mlbb_community_serializer
    lookup_field = "community_id"

class Create_mlbb_community_membership_view(generics.ListCreateAPIView):
    queryset = models.mlbb_Membership.objects.all()
    serializer_class = serializers.Mlbb_membership_serializer

class Mlbb_community_view(generics.ListAPIView):
    serializer_class = serializers.Mlbb_community_serializer

    def get_queryset(self):
        try:
            return models.mlbb_community.objects.all()
        except ObjectDoesNotExist:
            return Response({"error": "mlbb_squad not found"}, status=status.HTTP_404_NOT_FOUND)


class Apply_to_community_view(generics.ListCreateAPIView):
    queryset = models.mlbb_community_Application.objects.all()
    serializer_class = serializers.Mlbb_commmunity_application_Serializer


class Update_community_application_view(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.mlbb_community_Application.objects.all()
    serializer_class = serializers.Mlbb_commmunity_application_Serializer
    lookup_field = "mlbb_community_id"
