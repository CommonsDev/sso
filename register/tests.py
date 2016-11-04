from django.test import TestCase


class NextRedirectTest(TestCase):
    def test_next_param_is_session_saved(self):
        self.client.get('/login/?next=https://sso/')
        self.assertEqual(self.client.session.get('next'), 'https://sso/')
