from django.test import RequestFactory, TestCase
from django.contrib.auth.models import AnonymousUser, User
from .models import Quizzes, Question, Answer, Comment
from .views import Home, QuizzesView, QuestionView


class QuizzesViewTest(TestCase):
    """QuizzesViewTest - class for test quizzes views"""

    def setUp(self):
        self.user = User.objects.create_user(
            username="test_user",
            email='test_user@gmail.com',
            password='test_user_secret',
            first_name='Joe',
            last_name='Doe'
        )
        self.quizzes = Quizzes.objects.create(
            title="Test",
            q_person=self.user,
            content="Test Quizzes",
            is_publ=True
        )
        self.factory = RequestFactory()

    def test_home(self):
        request = self.factory.get('/')
        request.user = self.user
        response = Home.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_add_quizzes(self):
        request = self.factory.get('/quizzes/')
        request.user = self.user
        response = QuizzesView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_view_quizzes(self):
        request = self.factory.get('quizzes/%s' % self.quizzes.id)
        request.user = self.user
        response = QuizzesView.as_view()(request)
        self.assertEqual(response.status_code, 200)


class QuizzesTestCase(TestCase):
    """QuizzesTestCase - class for quizzes test case"""

    def setUp(self):
        self.user = User.objects.create_user(
            username="test_user",
            email='test_user@gmail.com',
            password='test_user_secret',
            first_name='Joe',
            last_name='Doe'
        )
        self.quizzes = Quizzes.objects.create(
            title="Test",
            q_person=self.user,
            content="Test Quizzes",
            is_publ=True
        )

    def test_quizzes_id(self):
        """test_quizzes_id - Quizzes id test"""
        self.assertEqual(
            self.quizzes.id,
            1
        )

    def test_quizzes_str(self):
        """test_quizzes_str - Quizzes string test"""
        self.assertEqual(
            self.quizzes.__str__(),
            '<Quizzes #1 from user #1>'
        )
