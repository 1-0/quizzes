from django.test import Client, TestCase
from django.contrib.auth.models import User
from .models import Quizzes, Question, Answer, Comment


def test_page(self, page):
    c = Client()
    resp = c.get('/home/')
    self.assertEqual(resp.status_code, 200)


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
        test_page(self, '/')

    def test_admin(self):
        test_page(self, '/admin/')

    def test_add_quizzes(self):
        test_page(self, '/quizzes/')

    def test_view_quizzes(self):
        test_page(self, '/quizzes/%s' % (QuizzesViewTest.quizzes.id, ))


class QuizzesTestCase(TestCase):
    """QuizzesTestCase - class for test case"""
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
        self.assertEqual(QuizzesTestCase.quizzes.__str__(), '<Quizzes #1 from user #1>')
