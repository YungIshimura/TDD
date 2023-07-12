from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from lists.views import view_index

class HomePageTest(TestCase):
    '''Тест домашней страницы'''

    def test_root_url_resolves_to_home_page_view(self):
        '''Корневой url преобразуется в представление домашней страницы'''
        found = resolve('/')
        self.assertEqual(found.func, view_index)
    
    def test_home_page_returns_correct_html(self):
        '''Тест: домашняя страница возвращает правильный html'''
        request = HttpRequest()
        response = view_index(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))