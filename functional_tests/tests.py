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
        self.assertIn('Is this a quiz?', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Questions', header_text)

        # He read a first question.
        question_text = self.browser.find_element_by_id('1').text
        self.assertEqual(question_text, '1. 1 Kg. = 1000 g. ?')
        # He answer yes
        radio = self.browser.find_element_by_id('id_yes_1')
        radio.click()

        # Then he click submit button
        button = self.browser.find_element_by_id('id_submit')
        button.click()

        # He has found 8 in answer textbox
        answer = self.browser.find_element_by_tag_name('h2').text
        self.assertEqual(answer, 'answer: 8')


