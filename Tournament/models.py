from django.db import models
from mlbb_app.models import mlbb_squad

class CreateTournament(models.Model):
    tournament_id = models.AutoField(primary_key=True)
    tournament_name = models.CharField(max_length=100)
    tournament_description = models.CharField(max_length=100)
    tournament_type = models.CharField(max_length=100)  # free/ paid
    tournament_image = models.ImageField(upload_to='tournaments/', blank=True, null=True)
    Game = models.CharField(max_length=100)
    max_no_participants = models.IntegerField()
    tournament_stages = models.CharField(max_length=100)  # single stage - double stage
    tournament_format = models.CharField(max_length=100)  # round robin, single elimination double elimination, swiss, free for all, leaderborard
    start_date = models.DateField(null=True, blank=True)
    registration_fee = models.IntegerField()

    class Meta:
        db_table = 'tournaments'



class ParticipatingTeam(models.Model):
    tournament = models.ForeignKey(CreateTournament, on_delete=models.CASCADE)
    participant_id = models.ForeignKey(mlbb_squad, on_delete=models.CASCADE)

    class Meta:
        db_table = 'participating_team'




class Match(models.Model):
    tournament = models.ForeignKey(CreateTournament, on_delete=models.CASCADE)
    team1 = models.ForeignKey(ParticipatingTeam, on_delete=models.CASCADE, related_name='matches_as_team1')
    team2 = models.ForeignKey(ParticipatingTeam, on_delete=models.CASCADE, related_name='matches_as_team2')
    team1_score = models.IntegerField( null=True, blank=True)
    team2_score = models.IntegerField( null=True, blank=True)
    match_date = models.DateField(null=True, blank=True)
    winner = models.ForeignKey(ParticipatingTeam, on_delete=models.SET_NULL, null=True, related_name='matches_won')
    match_round = models.IntegerField()  # Round in the tournament this match is held

    class Meta:
        db_table = 'matches'


class Bracket(models.Model):
    bracket_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    matches = models.ManyToManyField(Match, blank=True)
    tournament = models.ForeignKey(CreateTournament, on_delete=models.CASCADE, related_name="brackets")
    parent_bracket = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    total_round_number = models.IntegerField(default=1)
    winner = models.ForeignKey(ParticipatingTeam, on_delete=models.SET_NULL, null=True, blank=True)






