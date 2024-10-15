from django.shortcuts import render
from rest_framework import generics
from Tournament import models
from Tournament import serializers



class Create_Tournament_view(generics.ListCreateAPIView):
    queryset = models.CreateTournament.objects.all()
    serializer_class = serializers.Create_Tournament_Serializer


class Edit_tournament_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CreateTournament.objects.all()
    serializer_class = serializers.Create_Tournament_Serializer
    lookup_field = 'tournament_id'


class Tournament_participants_view(generics.ListCreateAPIView):
    queryset = models.ParticipatingTeam.objects.all()
    serializer_class = serializers.Tournament_Participant_Serializer

class Edit_tournament_participants_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ParticipatingTeam.objects.all()
    serializer_class = serializers.Tournament_Participant_Serializer
    lookup_field = 'participant_id'


class All_tournaments_view(generics.ListAPIView):
    queryset = models.CreateTournament.objects.all()
    serializer_class = serializers.Create_Tournament_Serializer

class Match_view(generics.ListCreateAPIView):
    queryset = models.Match.objects.all()
    serializer_class = serializers.Match_serializer


class Match_update_view(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Match.objects.all()
    serializer_class = serializers.Match_serializer
    lookup_field = 'id'


class Bracket_view(generics.ListCreateAPIView):
    queryset = models.Bracket.objects.all()
    serializer_class = serializers.Bracket_serializer

class Bracket_update_view(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Bracket.objects.all()
    serializer_class = serializers.Bracket_serializer
    lookup_field = "bracket_id"


