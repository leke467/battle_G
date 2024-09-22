from player_Account.models import Account
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from squad_app.models import GameSquad, GameSquadApplicationBase, GameSquadInviteBase

class mlbb_profile(models.Model):
    """

    The `mlbb_profile` class represents a model in the `mlbb_app` app that stores information about Mobile Legends: Bang Bang player profiles.

    """
    mlbb_player_id = models.CharField(primary_key=True, max_length=50)
    mlbb_player_ign = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    squad_id = models.ForeignKey('mlbb_squad', on_delete=models.CASCADE, null=True, blank=True)
    Account_id = models.OneToOneField(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.mlbb_player_ign

    class Meta:
        app_label = 'mlbb_app'
        db_table = 'mlbb_profile'

class mlbb_squad(GameSquad):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    profile = GenericForeignKey('content_type', 'object_id')

    class Meta:
        db_table = 'mlbb_squads'

class mlbb_Squad_Application(GameSquadApplicationBase):
    squad = models.ForeignKey(mlbb_squad, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'squad_applications'

class mlbb_Squad_Invite(GameSquadInviteBase):
    squad = models.ForeignKey(mlbb_squad, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'squad_invites'
