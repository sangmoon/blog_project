from .base import FuntionalTest


class NewArticleTest(FuntionalTest):

    def tset_can_not_write_article_without_login(self):
        pass

    def test_can_write_new_article(self):

        test_title = 'test_title'
        test_content = 'test_content'

        self.browser.find_element_by_id('id_title').send_keys(
            test_title)
        self.browser.find_element_by_id('id_content').send_keys(
            test_content)
        self.browser.find_element_by_id('submit').click()
