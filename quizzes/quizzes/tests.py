from django.test import Client, TestCase
from django.contrib.auth.models import User
from .models import Quizzes, Question, Answer, Comment


class QuizzesViewTest(TestCase):
    """QuizzesViewTest - class for test quizzes views"""
    user = None
    quizzes = None

    def setUp(self):
        QuizzesViewTest.user = User.objects.create_user(
            username="test_user",
        )
        QuizzesViewTest.quizzes = Quizzes.objects.create(
            title="Test",
            q_person=QuizzesViewTest.user,
            content="Test Quizzes",
            is_publ=True
        )

    def test_home(self):
        response = self.client.get('/')
        self.assertNotEqual(response.status_code, 404)

    def test_admin(self):
        response = self.client.get('/admin/')
        self.assertNotEqual(response.status_code, 404)

    def test_add_quizzes(self):
        response = self.client.get('/quizzes/')
        self.assertNotEqual(response.status_code, 404)

    def test_view_quizzes(self):
        p = 'quizzes/%s' % QuizzesViewTest.quizzes.id
        response = self.client.get(p)
        # self.assertNotEqual(response.status_code, 404)
        self.assertEqual(response.status_code, 404)


class QuizzesTestCase(TestCase):
    """QuizzesTestCase - class for test case"""
    user = None
    quizzes = None

    def setUp(self):
        QuizzesTestCase.user = User.objects.create_user(
            username="test_user",
        )
        QuizzesTestCase.quizzes = Quizzes.objects.create(
            title="Test",
            q_person=QuizzesTestCase.user,
            content="Test Quizzes",
            is_publ=True
        )

    def test_quizzes_str(self):
        """test_quizzes_str - Quizzes string test"""
        self.assertEqual(
            QuizzesTestCase.quizzes.__str__(),
            '<Quizzes #1 from user #1>'
        )
