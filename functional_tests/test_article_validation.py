from .base import FuntionalTest
from django.contrib.auth.models import User


class NewVisitorTest(FuntionalTest):

    def test_can_start_a_page_and_log_in(self):
        test_title = 'test_title'
        test_content = 'test_content'

        self.browser.find_element_by_id('id_title').send_keys(
            test_title)
        self.browser.find_element_by_id('id_content').send_keys(
            test_content)
        self.browser.find_element_by_id('submit').click()
