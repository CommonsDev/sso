from django.test import TestCase
from django.core import mail
from django.contrib.auth import get_user_model

User = get_user_model()


class NextRedirectTest(TestCase):
    def test_next_param_is_session_saved(self):
        self.client.get('/login/?next=https://sso/')
        self.assertEqual(self.client.session.get('next'), 'https://sso/')


class AccountWizardTest(TestCase):
    def test_login_home(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'id="id_email"')
        self.assertNotContains(response, 'id="id_password"')

    def test_create_account(self):
        response = self.client.post('/login/?next=https://sso/',
                                    {'email': 'local@test.dev'},
                                    follow=True)
        self.assertRedirects(response, '/auth/register/')
        self.assertContains(response, 'local@test.dev')
        self.assertContains(response, 'id="id_password1"')
        self.assertContains(response, 'Create account')

        response = self.client.post('/auth/register/', {'password1': 'test'},
                                    follow=True)
        self.assertRedirects(response, '/register/complete/')
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('/?next=https://sso/', mail.outbox[0].body)

    def test_login_account(self):
        user = User.objects.create(email='local@test.dev', is_active=True)
        user.set_password('test')
        user.save()

        response = self.client.post('/login/', {'email': 'local@test.dev'},
                                    follow=True)
        self.assertRedirects(response, '/auth/login/')
        self.assertContains(response, 'local@test.dev')
        self.assertContains(response, 'id="id_password"')
        self.assertContains(response, 'Log in')

        response = self.client.post('/auth/login/', {'password': 'test'},
                                    follow=True)
        self.assertRedirects(response, 'https://sso/')
