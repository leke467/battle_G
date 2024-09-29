from django.db import models
from squad_app import models as squad_app_models

# Create your models here.
class community(models.Model):
    community_id = models.AutoField(primary_key=True)
    community_tag = models.CharField(max_length=255, null=False, unique=True)
    community_name = models.CharField(max_length=50)
    community_description = models.TextField()
    community_image = models.ImageField(upload_to='images/')
    leader = models.ForeignKey('mlbb_app.mlbb_profile', on_delete=models.CASCADE, related_name='squad_leader')
    applicants = models.ManyToManyField()
    squads = models.ManyToManyField(squad_app_models.GameSquad, through="Membership")


class Membership(models.Model):
    squad = models.ForeignKey(squad_app_models.GameSquad, on_delete=models.CASCADE)
    community = models.ForeignKey(community, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)
