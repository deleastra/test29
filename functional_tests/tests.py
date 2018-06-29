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
        # เข้าเว็ปไซต์
        self.browser.get(self.live_server_url)


        # He notices website title and header.
        # assert header ของ website ว่าถูกต้องหรือไม่
        self.assertIn('Answer or Question', self.browser.title)
        # เมื่อทดสอบผ่านหมายความว่าสามารถเข้าเว็ปไซต์ได้ตามที่ต้องการ

        # ---------------ทดสอบการสร้างคำถาม-----------------
        # He want to create 3 questions.
        # so click the create question button.
        # สร้าง list ขึ้นมาเพื่อเก็บคำถามและคำตอบที่ต้องการจะสร้าง
        questions = [['Is 1 kg. = 1000 g.?', 'yes'],
                     ['Is 1 day have 20 hours?', 'no'],
                     ['Is 1 week have 7 days', 'yes']]

        # สร้างคำถามโดยใช้ข้อมูลจากคำถามที่สร้างเอาไว้ใน list
        for question in questions:
            # Click create question button.
            # กดปุ่มสร้างคำถาม
            button = self.browser.find_element_by_id('id_create')
            button.click()
            
            # Ask question.
            # เขียนข้อความคำถามลงใน text box 
            inputbox = self.browser.find_element_by_id('id_question')
            inputbox.send_keys(question[0])

            # เลือกคำตอบที่ถูกต้องโดยต้องเลือกที่ radio ถ้าเป็น yes ให้เลือก id เป็น id_yes และถ้าเป็น no ให้เลือก id เป็น id_no 
            button = self.browser.find_element_by_id('id_' + question[1])
            button.click()

            # Submit question.
            # กดยืนยันการสร้าคำถาม
            button = self.browser.find_element_by_id('id_submit')
            button.click()

        # เมื่อทดสอบผ่านแสดงว่าสามารถสร้างคำถามได้แล้ว

        # ----------------ทดสอบการตอบคำถาม--------------------     
        # Bob had finish ask the questions.
        # Then he go to invite his friend to answer his questions.
        
        # Bob had invite Cid to answer his questions.
        # So Cid open browser and go Quiz website.
        
        # Then he go to answer questions.
        # ไปที่หน้าตอบคำถาม
        button = self.browser.find_element_by_id('id_answer')
        button.click()

        # สร้าง list คำถามและคำตอบที่ต้องการจะตอบ
        answers = [['Is 1 kg. = 1000 g.?', 'yes'],
                     ['Is 1 day have 20 hours?', 'yes'],
                     ['Is 1 week have 7 days', 'no']]
        
        for i in range(3):

            # He read a question.
            # assert ดูว่าคำถามตรงกับที่ต้องการหรือไม่
            question_text = self.browser.find_element_by_id(i).text
            self.assertEqual(question_text[3:], answers[i][0])

            # then answer.
            # เลือกคำตอบ yes หรือ no เมื่อ yes จะมี id เป็น id_yes_ ตามด้วยลำดับของคำถามเริ่มตั้งแต่ id_yes_0
            # ถ้าหากเลือก no จะมี id เป็น id_no_ ตามด้วยลำดับของคำถามเริ่มตั้งแต่ id_no_0
            radio = self.browser.find_element_by_id('id_' + answers[i][1] + '_' + str(i))
            radio.click()

        # Then he click submit button
        # กดยืนยันการตอบคำถาม เมื่อกดตอบคำถามแล้วก็จะมีคะแนนเพิ่มขึ้นมา
        button = self.browser.find_element_by_id('id_submit')
        button.click()

        # Score has showing
        # assert คะแนนจะต้องเท่ากับ 1
        score = self.browser.find_element_by_tag_name('h2').text
        self.assertEqual(score, 'Your score is 1.')
        # เมื่อทดสอบจุดนี้ผ่านหมายความว่าสามารถตอบคำถามและแสดงคำตอบได้แล้ว

        # กดปุ่ม back เพื่อไปที่ homepage
        button = self.browser.find_element_by_id('id_back')
        button.click()
        
        # After Cid had see score he dissatisfied with the score.
        # So he hot headed and close the browser.

        # Next day.
        # Cid had prepare himself for any questions.
        # He open browser and open Quiz website.

        # -------------------ทดสอบการตอบคำถามอีกครั้ง------------------------
        # Then he go to answer questions.
        button = self.browser.find_element_by_id('id_answer')
        button.click()

        # สร้างคำถามโดยคำถามเหมือนก่อนหน้านี้แต่คำตอบเปลี่ยนไป
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

        # เมื่อผ่านถึงจุดนี้แสดงว่าสามารถตอบคำถามได้อีกครั้งโดยคะแนนแตกต่างกัน
        
        # All correct.
        # Cid have satisfied with the score.
        # Then he call Bob to see his score.
        # Bob had shock after see his score.
        # so he want to know is it first time he answer his questions.

        # He clicked back button.
        button = self.browser.find_element_by_id('id_back')
        button.click()

        # -------------------------ทดสอบหน้าสถิติการตอบคำถาม--------------------------
        # He clicked statistics button.
        # เข้ามาที่หน้าสถิติ
        button = self.browser.find_element_by_id('id_statistics')
        button.click()

        # He have seen quiz statistics table.
        # ตรวจสอบดูว่ามีตารางสถิติอยู่หรือไม่
        table = self.browser.find_element_by_id('id_quiz_statistics')

        # He look for quiz statistics.
        # ทดสอบอ่านค่าในตาราง
        rows = table.find_elements_by_tag_name('tr')

        # ใส่ข้อมูลที่ต้องการจะทดสอบไว้ใน list
        # โดยข้อมูลที่ทดสอบก็มาจากการตอบคำถามที่ผ่านมาว่าตอบถูกและตอบผิดกี่ครั้ง
        questions = ['1: Is 1 kg. = 1000 g.? 2 0',
                     '2: Is 1 day have 20 hours? 1 1',
                     '3: Is 1 week have 7 days 1 1']

        # ตรวจสอบตารางทีละแถวว่ามีข้อความขึ้นตรงกับที่ต้องการหรือไม่
        for i in range(len(questions)):
            self.assertEqual(questions[i], rows[i+1].text)

        # So Bob know Cid didn't do that quiz first time.
        # เมื่อทดสอบผ่านถึงจุดนี้แล้วแสดงว่าหน้าสถิติแสดงข้อมูลได้ถูกต้อง
