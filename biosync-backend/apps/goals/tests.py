from datetime import date

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()


class BioSyncApiTests(APITestCase):
    def register(self, email, username):
        response = self.client.post('/api/v1/users/register/', {
            'email': email, 'username': username, 'first_name': 'Test', 'last_name': 'User',
            'password': 'Str0ng-pass!', 'password2': 'Str0ng-pass!',
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
        return response.data['token']

    def use(self, token):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')

    def create_goal(self, target='10'):
        response = self.client.post('/api/v1/goals/', {
            'title': 'Run 10 km', 'start_date': str(date.today()), 'target_value': target,
            'target_unit': 'km', 'goal_type': 'Fitness',
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
        return response.data

    def test_requires_authentication(self):
        self.assertEqual(self.client.get('/api/v1/goals/').status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_with_email(self):
        self.register('ann@example.com', 'ann')
        response = self.client.post('/api/v1/users/login/', {'email': 'ann@example.com', 'password': 'Str0ng-pass!'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        self.assertIn('token', response.data)

    def test_progress_updates_goal(self):
        self.use(self.register('ann@example.com', 'ann'))
        goal = self.create_goal(target='10')
        response = self.client.post('/api/v1/progress/', {'goal': goal['id'], 'date': str(date.today()), 'value': '4'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
        goal = self.client.get(f"/api/v1/goals/{goal['id']}/").data
        self.assertEqual(goal['status'], 'IN_PROGRESS')
        self.assertEqual(float(goal['progress_percentage']), 40.0)

    def test_users_only_see_and_update_their_own_goals(self):
        self.use(self.register('ann@example.com', 'ann'))
        goal = self.create_goal()
        self.use(self.register('bob@example.com', 'bob'))
        self.assertEqual(len(self.client.get('/api/v1/goals/').data), 0)
        self.assertEqual(self.client.get(f"/api/v1/goals/{goal['id']}/").status_code, status.HTTP_404_NOT_FOUND)
        # Bob can't log progress against Ann's goal
        response = self.client.post('/api/v1/progress/', {'goal': goal['id'], 'date': str(date.today()), 'value': '5'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
