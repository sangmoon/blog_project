from .base import FuntionalTest
from django.contrib.auth.models import User


class NewVisitorTest(FuntionalTest):

    def test_can_start_a_page_and_log_in(self):
        # sangmoon come into this homepage.
        # He check out title and main message
        self.browser.get(self.server_url)
        self.assertIn('SM blog', self.browser.title)
        head_text = self.browser.find_element_by_tag_name('h3').text
        self.assertIn('박상문님의 블로그입니다.', head_text)

    def test_can_log_in(self):
        # He try to log_in.
        self.browser.get(self.server_url)
        username = 'test'
        password = 'secret'
        user = self.makeTestUser(username, password)
        # self.assertEqual(user, User.objects.get(username='test'))

        '''
        login_successful = self.client.login(
            username=username, password=password)
        self.assertTrue(login_successful)
        '''
        self.browser.find_element_by_id('log_in').click()

        self.browser.find_element_by_id('id_username').send_keys(username)
        self.browser.find_element_by_id('id_password').send_keys(password)
        self.browser.find_element_by_id('submit').click()

        self.assertTrue(self.browser.find_element_by_id('log_out'))

    def test_log_in_and_out_redirect_prev_page(self):
        # He go to about page,
        # and log_in
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('about').click()

        self.assertEqual(
            self.browser.current_url,
            self.server_url + '/about',
        )

        username = 'test'
        password = 'secret'
        user = self.makeTestUser(username, password)

        self.browser.find_element_by_id('log_in').click()
        self.browser.find_element_by_id('id_username').send_keys(username)
        self.browser.find_element_by_id('id_password').send_keys(password)
        self.browser.find_element_by_id('submit').click()

        self.assertEqual(
            self.browser.current_url,
            self.server_url + '/about',
        )

        self.browser.find_element_by_id('log_out').click()

        self.assertEqual(
            self.browser.current_url,
            self.server_url + '/about',
        )
