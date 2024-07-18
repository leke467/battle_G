from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class GameSquad(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    profile = GenericForeignKey('content_type', 'object_id')
    squad_name = models.CharField(max_length=50)
    squad_id = models.IntegerField(primary_key=True)
    squad_tag = models.CharField(max_length=50)
    squad_logo = models.ImageField(upload_to='squad_logo', null=True, blank=True)
    squad_country = models.CharField(max_length=50)
    applications = models.ManyToManyField('mlbb_app.mlbb_profile', related_name='squad_applications', blank=True)
    invites = models.ManyToManyField('mlbb_app.mlbb_profile', related_name='squad_invites')
    leader = models.ForeignKey('mlbb_app.mlbb_profile', on_delete=models.CASCADE, related_name='squad_leader')
    members = models.ManyToManyField('mlbb_app.mlbb_profile', related_name='squad_members')

    class Meta:
        abstract = True

class GameSquadApplicationBase(models.Model):
    user = models.ForeignKey('mlbb_app.mlbb_profile', on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='pending')

    class Meta:
        abstract = True

class GameSquadInviteBase(models.Model):
    user = models.ForeignKey('mlbb_app.mlbb_profile', on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='pending')

    class Meta:
        abstract = True
