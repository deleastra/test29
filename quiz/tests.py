from django.urls import resolve
from django.test import TestCase
from quiz.views import homepage, create, answer, statistic
from quiz.models import Quiz

# Create your tests here.

class HomepageTests(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, homepage)

    def test_homepage_uses_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'homepage.html')

class CreatepageTest(TestCase):
    def test_create_url_resolves_to_create_page_view(self):
        found = resolve('/quiz/create')
        self.assertEqual(found.func, create)

    def test_create_uses_template(self):
        response = self.client.get('/quiz/create')
        self.assertTemplateUsed(response, 'create.html')

class AnswerpageTest(TestCase):
    def test_answer_url_resolves_to_answer_page_view(self):
        found = resolve('/quiz/answer')
        self.assertEqual(found.func, answer)

    def test_answer_uses_template(self):
        response = self.client.get('/quiz/answer')
        self.assertTemplateUsed(response, 'answer.html')

class StatisticspageTest(TestCase):
    def test_statistics_url_resolves_to_statistics_page_view(self):
        found = resolve('/quiz/statistics')
        self.assertEqual(found.func, statistic)

    def test_statistics_uses_template(self):
        response = self.client.get('/quiz/statistics')
        self.assertTemplateUsed(response, 'statistic.html')        
        
class QuizModelTests(TestCase):
    def test_can_create_model_quiz(self):
        Quiz.objects.create(question='question', answer=True)
        saved_quiz = Quiz.objects.all()
        self.assertEqual(saved_quiz.count(), 1)

    def test_quiz_model_can_count_correct_times(self):
        Quiz.objects.create(question='question', answer=True)
        saved_quiz = Quiz.objects.get(pk=1)
        saved_quiz.correct += 1
        saved_quiz.save()
        self.assertEqual(saved_quiz.correct, 1)
        self.assertEqual(saved_quiz.incorrect, 0)

    def test_quiz_model_can_count_incorrect_times(self):
        Quiz.objects.create(question='question', answer=True)
        saved_quiz = Quiz.objects.get(pk=1)
        saved_quiz.incorrect += 1
        saved_quiz.save()
        self.assertEqual(saved_quiz.incorrect, 1)
        self.assertEqual(saved_quiz.correct, 0)

class QuizTest(TestCase):
    def test_create_page_can_create_quiz(self):
        self.client.post('/quiz/create', data={'question':'test_question', 'answer': 'yes'})
        saved_quiz = Quiz.objects.all()
        self.assertEqual(saved_quiz.count(), 1)

    def test_answer_page_can_answer_correct_quiz(self):
        Quiz.objects.create(question='question', answer=True)
        self.client.post('/quiz/answer', data={'csrffake': 'xxxxxx', 'answer_1': 'yes'})
        saved_quiz = Quiz.objects.get(pk=1)
        self.assertEqual(saved_quiz.correct, 1)
        self.assertEqual(saved_quiz.incorrect, 0)

    def test_answer_page_can_answer_incorrect_quiz(self):
        Quiz.objects.create(question='question', answer=True)
        self.client.post('/quiz/answer', data={'csrffake': 'xxxxxx', 'answer_1': 'false'})
        saved_quiz = Quiz.objects.get(pk=1)
        self.assertEqual(saved_quiz.correct, 0)
        self.assertEqual(saved_quiz.incorrect, 1)
