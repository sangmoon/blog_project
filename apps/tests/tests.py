from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from apps.views import home_page
from apps.models import Article


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<!DOCTYPE html>'))
        self.assertIn(b'<title>SM blog</title>', response.content)
        self.assertTrue(response.content.strip().endswith(b'</html>'))


class ArticleModelTest(TestCase):

    def test_saving_and_retreiving_article(self):
        pass