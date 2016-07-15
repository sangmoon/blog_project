from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
from django.contrib.auth.models import User


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_page_and_log_in(self):
        # sangmoon come into this homepage.
        self.browser.get(self.live_server_url)

        # He check out title and main message
        self.assertIn('SM blog', self.browser.title)
        head_text = self.browser.find_element_by_tag_name('h3').text
        self.assertIn('박상문님의 블로그입니다.', head_text)

        # He try to write a article but is sent to login page.

        username = 'test'
        password = 'secret'
        user = User.objects.create_user(
            username=username, password=password
        )

        self.assertEqual(user, User.objects.get(username='test'))
        '''
        login_successful = self.client.login(
            username=username, password=password)
        self.assertTrue(login_successful)
        '''
        link = self.browser.find_element_by_id('write_link')
        link.click()

        self.assertEqual(
            self.browser.current_url,
            self.live_server_url + "/login?next=/write"
        )

        username_box = self.browser.find_element_by_id('id_username')
        password_box = self.browser.find_element_by_id('id_password')
        login_key = self.browser.find_element_by_id('submit')

        username_box.send_keys(username)
        password_box.send_keys(password)
        login_key.click()

        self.assertTrue(self.browser.find_element_by_id('log_out'))

        title_box = self.browser.find_element_by_id('id_title')
        content_box = self.browser.find_element_by_id('id_content')
        submit_key = self.browser.find_element_by_id('submit')

        test_title = 'test_title'
        test_content = 'test_content'

        title_box.send_keys(test_title)
        content_box.send_keys(test_content)
        submit_key.click()

        # 여기서 원래 타이틀, 내용, 작성자랑 화면에 나오는 내용 맞는지 체크
        '''
        # self.assertEqual()

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item',
        )

        inputbox.send_keys('Buy peacock feathers')

        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id("id_list_table")
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )
        '''
        self.fail('Finish the test!')
