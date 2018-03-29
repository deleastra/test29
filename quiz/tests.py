from django.urls import resolve
from django.test import TestCase
from quiz.views import homepage
from .models import Quiz

# Create your tests here.

class HomepageTests(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, homepage)

    def test_homepage_uses_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'homepage.html')

class QuizModelTests(TestCase):
    def test_can_create_model_quiz(self):
        Quiz.objects.create(question='question', answer=True)
        saved_quiz = Quiz.objects.all()
        self.assertEqual(saved_quiz.count(), 1)

class CreateQuizTest(TestCase):
    def test_create_page_can_create_quiz(self):
        self.client.post('/quiz/create', data={'question':'test_question', 'answer': 'yes'})
        saved_quiz = Quiz.objects.all()
        self.assertEqual(saved_quiz.count(), 1)
