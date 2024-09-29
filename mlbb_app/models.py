from player_Account.models import Account
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

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

class mlbb_squad(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    profile = GenericForeignKey('content_type', 'object_id')
    squad_name = models.CharField(max_length=50)
    squad_id = models.IntegerField(primary_key=True)
    squad_tag = models.CharField(max_length=50)
    squad_logo = models.ImageField(upload_to='squad_logo', null=True, blank=True)
    squad_country = models.CharField(max_length=50)
    applications = models.ManyToManyField(mlbb_profile, related_name='squad_applications', blank=True)
    invites = models.ManyToManyField(mlbb_profile, related_name='squad_invites')
    leader = models.ForeignKey(mlbb_profile, on_delete=models.CASCADE, related_name='squad_leader')
    members = models.ManyToManyField(mlbb_profile, related_name='squad_members')
    tournament_won = models.IntegerField(default=0, blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    profile = GenericForeignKey('content_type', 'object_id')

    class Meta:
        db_table = 'mlbb_squads'

class mlbb_Squad_Application(models.Model):
    user = models.ForeignKey(mlbb_profile, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='pending')
    squad = models.ForeignKey(mlbb_squad, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'squad_applications'

class mlbb_Squad_Invite(models.Model):
    user = models.ForeignKey(mlbb_profile, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='pending')
    squad = models.ForeignKey(mlbb_squad, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'squad_invites'
