from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException
import time

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_user_can_answer_quiz(self):
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

        # After he create question then he go to answer questions.
        button = self.browser.find_element_by_id('id_answer')
        button.click()

        answers = [['Is 1 kg. = 1000 g.?', 'yes'],
                     ['Is 1 day have 20 hours?', 'no'],
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
        self.assertEqual(score, 'Your score is 2.')

