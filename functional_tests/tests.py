from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException
import time

class QuizTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_user_can_ask_answer_and_see_statistics_questions(self):
        # Bob had hear abour new quiz game website.
        # He love quiz game so he open browser for that website.
        self.browser.get(self.live_server_url)


        # He notices website title and header.
        self.assertIn('Answer or Question', self.browser.title)

        # He want to create 3 questions.
        # so click the create question button.
        questions = [['Is 1 kg. = 1000 g.?', 'yes'],
                     ['Is 1 day have 20 hours?', 'no'],
                     ['Is 1 week have 7 days', 'yes']]

        for question in questions:
            # Click create question button.
            button = self.browser.find_element_by_id('id_create')
            button.click()
            
            # Ask question.
            inputbox = self.browser.find_element_by_id('id_question')
            inputbox.send_keys(question[0])

            button = self.browser.find_element_by_id('id_' + question[1])
            button.click()

            # Submit question.
            button = self.browser.find_element_by_id('id_submit')
            button.click()
            
        # Bob had finish ask the questions.
        # Then he go to invite his friend to answer his questions.
        
        # Bob had invite Cid to answer his questions.
        # So Cid open browser and go Quiz website.
        
        # Then he go to answer questions.
        button = self.browser.find_element_by_id('id_answer')
        button.click()

        answers = [['Is 1 kg. = 1000 g.?', 'yes'],
                     ['Is 1 day have 20 hours?', 'yes'],
                     ['Is 1 week have 7 days', 'no']]
        
        for i in range(3):

            # He read a question.
            question_text = self.browser.find_element_by_id(i).text
            self.assertEqual(question_text[3:], answers[i][0])

            # then answer.
            radio = self.browser.find_element_by_id('id_' + answers[i][1] + '_' + str(i))
            radio.click()

        # Then he click submit button
        button = self.browser.find_element_by_id('id_submit')
        button.click()

        # Score has showing
        score = self.browser.find_element_by_tag_name('h2').text
        self.assertEqual(score, 'Your score is 1.')

        button = self.browser.find_element_by_id('id_back')
        button.click()
        
        # After Cid had see score he dissatisfied with the score.
        # So he hot headed and close the browser.

        # Next day.
        # Cid had prepare himself for any questions.
        # He open browser and open Quiz website.

        # Then he go to answer questions.
        button = self.browser.find_element_by_id('id_answer')
        button.click()

        answers = [['Is 1 kg. = 1000 g.?', 'yes'],
                     ['Is 1 day have 20 hours?', 'no'],
                     ['Is 1 week have 7 days', 'yes']]

        for i in range(3):

            # He read a question.
            question_text = self.browser.find_element_by_id(i).text
            self.assertEqual(question_text[3:], answers[i][0])

            # then answer.
            radio = self.browser.find_element_by_id('id_' + answers[i][1] + '_' + str(i))
            radio.click()

        # Then he click submit button
        button = self.browser.find_element_by_id('id_submit')
        button.click()

        # Score has showing
        score = self.browser.find_element_by_tag_name('h2').text
        self.assertEqual(score, 'Your score is 3.')

        # All correct.
        # Cid have satisfied with the score.
        # Then he call Bob to see his score.
        # Bob had shock after see his score.
        # so he want to know is it first time he answer his questions.

        # He clicked back button.
        button = self.browser.find_element_by_id('id_back')
        button.click()

        # He clicked statistics button.
        button = self.browser.find_element_by_id('id_statistics')
        button.click()

        # He have seen quiz statistics table.
        table = self.browser.find_element_by_id('id_quiz_statistics')

        # He look for quiz statistics.
        rows = table.find_elements_by_tag_name('tr')

        questions = ['1: Is 1 kg. = 1000 g.? 2 0',
                     '2: Is 1 day have 20 hours? 1 1',
                     '3: Is 1 week have 7 days 1 1']

        for i in range(len(questions)):
            self.assertEqual(questions[i], rows[i+1].text)

        # So Bob know Cid didn't do that quiz first time.
