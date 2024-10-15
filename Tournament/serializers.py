from rest_framework import serializers
from Tournament import models


class Create_Tournament_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.CreateTournament
        fields = "__all__"


class Tournament_Participant_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.ParticipatingTeam
        fields = "__all__"


class Match_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Match
        fields = "__all__"


class Bracket_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bracket
        fields = "__all__"

