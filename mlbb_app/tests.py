from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.urls import reverse
from .models import mlbb_squad

class MLBBTestCase(APITestCase):
    def setUp(self):
        # Creating a test client
        self.client = APIClient()
        # Creating test user and squad owner
        self.test_user = User.objects.create_user(username='testuser', password='testpassword')
        self.squad_owner = User.objects.create_user(username='squadowner', password='ownerpassword')
        # Creating token for test user and squad owner
        self.token_test_user = Token.objects.create(user=self.test_user)
        self.token_squad_owner = Token.objects.create(user=self.squad_owner)
        # Creating test squad
        self.squad = mlbb_squad.objects.create(squad_name="test_squad", leader=self.squad_owner)
        ...

    # replace ... with other required values if need be
    # Then, define each individual test, for example:
    def test_squad_application(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_test_user.key)
        response = self.client.post(reverse('mlbb/squads/apply/', kwargs={'squad_id': self.squad.squad_id}),
                                    {'squad': self.squad.squad_id})
        self.assertEqual(response.status_code, 200)

    def test_squad_invitation(self):
        # assuming you are inviting 'test_user' to the squad owned by 'squad_owner'
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_squad_owner.key)
        response = self.client.post(reverse('mlbb/squads/invites/', kwargs={'squad_id': self.squad.squad_id}),
                                    {'squad': self.squad.squad_id, 'user': self.test_user.id})
        self.assertEqual(response.status_code, 200)
