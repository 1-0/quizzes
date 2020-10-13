import datetime
from django.test import RequestFactory, TestCase
from django.contrib.auth.models import AnonymousUser, User
from .models import UserCard, QuizzesProgress
from .views import show_user


class UserCardViewTest(TestCase):
    """UserCardViewTest - class for test UserCard views"""

    def setUp(self):
        self.user = User.objects.create_user(
            username="test_user",
            email='test_user@gmail.com',
            password='test_user_secret',
            first_name='Joe',
            last_name='Doe'
        )
        self.user_card = UserCard.objects.create(
            person=self.user,
            birthday=datetime.date(1970, 1, 1),
            about="Test User About",
        )
        self.factory = RequestFactory()

    def test_show_user(self):
        request = self.factory.get('/usercards/show_user/%s' % (self.user.username,))
        request.user = self.user
        response = show_user(request, self.user.username)
        self.assertEqual(response.status_code, 200)


class UserCardTestCase(TestCase):
    """UserCardTestCase - class for UserCard test case"""

    def setUp(self):
        self.user = User.objects.create_user(
            username="test_user",
            email='test_user@gmail.com',
            password='test_user_secret',
            first_name='Joe',
            last_name='Doe'
        )
        self.user_card = UserCard.objects.create(
            person=self.user,
            birthday=datetime.date(1970, 1, 1),
            about="Test User About",
        )
        self.factory = RequestFactory()

    def test_user_card_person_id(self):
        """test_user_card_person_id - UserCard person id test"""
        self.assertEqual(
            self.user_card.person.id,
            1
        )

    def test_user_card_str(self):
        """test_quizzes_str - UserCard string test"""
        self.assertEqual(
            self.user_card.__str__(),
            '<UserCard #1 for user #1>'
        )
