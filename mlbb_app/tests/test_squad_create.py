from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from mlbb_app.models import mlbb_profile, mlbb_squad
from mlbb_app.serializers import mlbb_squadSerializer

class TestMlbbSquadCreate(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.profile = mlbb_profile.objects.create(user=self.user)
        self.data = {
            'squad_name': 'Test Squad',
            'squad_tag': 'TS',
            'squad_country': 'USA',
        }

    def test_create_squad(self):
        response = self.client.post(reverse('mlbb_squad_create'), data=self.data)
        self.assertEqual(response.status_code, 201)
        squad = mlbb_squad.objects.get(squad_name='Test Squad')
        self.assertEqual(squad.leader, self.profile)
        self.assertEqual(squad.leader_id, self.profile.mlbb_id)
        self.assertEqual(squad.members.count(), 1)
        self.assertIn(self.profile, squad.members.all())

