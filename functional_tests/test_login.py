
from .base import FuntionalTest
from django.contrib.auth.models import User


class NewVisitorTest(FuntionalTest):

    def test_can_start_a_page_and_log_in(self):
        # sangmoon come into this homepage.
        self.browser.get(self.server_url)

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
        self.browser.find_element_by_id('write_link').click()

        self.assertEqual(
            self.browser.current_url,
            self.server_url + "/login?next=/write"
        )

        self.browser.find_element_by_id('id_username').send_keys(username)
        self.browser.find_element_by_id('id_password').send_keys(password)
        self.browser.find_element_by_id('submit').click()

        self.assertTrue(self.browser.find_element_by_id('log_out'))

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
