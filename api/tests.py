import datetime
from django.utils import timezone

from oauth2_provider.tests.test_authorization_code import BaseTest
from oauth2_provider.models import AccessToken


class ProfileTest(BaseTest):

    def test_profile_access_requires_auth(self):
        response = self.client.get('/api/profile/')
        self.assertEquals(response.status_code, 302)

    def test_profile_data(self):
        token = AccessToken.objects.create(
            user=self.test_user, token='1234567890',
            application=self.application,
            expires=timezone.now() + datetime.timedelta(days=1),
            scope='read'
        )
        response = self.client.get(
            '/api/profile/', HTTP_AUTHORIZATION='Bearer {}'.format(token))
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.json()['id'], self.test_user.id)
        self.assertEquals(response.json()['email'], self.test_user.email)

    def test_access_with_wrong_token(self):
        AccessToken.objects.create(
            user=self.test_user, token='1234567890',
            application=self.application,
            expires=timezone.now() + datetime.timedelta(days=1),
            scope='read'
        )
        response = self.client.get(
            '/api/profile/', HTTP_AUTHORIZATION='Bearer 123')
        self.assertEquals(response.status_code, 401)
        self.assertIn('WWW-Authenticate', response)
