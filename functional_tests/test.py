from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time
from django.test import LiveServerTestCase

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):
    '''Tect нового посетителя'''
    
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()
    
    def tearDown(self) -> None:
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        '''Ожидание строки в таблице списка'''
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element('id', 'id_list_table')
                rows = table.find_elements('tag name', 'tr')
                self.assertIn(row_text, [row.text for row in rows])
                break

            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_and_retrieve_it_layer(self):
        '''Можно ли начать список и получить его позже'''
        # Некий гражданин слышал про новое крутое приложение со списком дел. Он хочет оценить его домашнюю страницу.
        self.browser.get(self.live_server_url)

        # Он видит, что заголовок и шапка страницы говорят о списках дел
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element('tag name', 'h1').text
        self.assertIn('To-Do', header_text)

        # Ему сразу же предлагается ввести элемент списка (дело)
        inputbox = self.browser.find_element('id', 'id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        # Она набирает в текстовом поле "Купить молоко"
        inputbox.send_keys('Купить молоко')

        # Когда она нажимает enter страница обновляется и теперь страницу содержит 1: "Купить молоко"
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.wait_for_row_in_list_table('1: Купить молоко')

        table = self.browser.find_element('id', 'id_list_table')
        rows = table.find_elements('tag name', 'tr')
        self.assertIn('1: Купить молоко', [row.text for row in rows])
        # Текстовое поле по прежнему предлагает ей добавить ещё один элемент списка. Она вводит "Купить кефир"
        
        inputbox = self.browser.find_element('id', 'id_new_item')
        inputbox.send_keys('Купить кефир')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # Страница снова обновляется и показывает оба элемента её списка
        self.wait_for_row_in_list_table('1: Купить молоко')
        self.wait_for_row_in_list_table('2: Купить кефир')
        # Гражданину интересно, запомнит ли сайт её список. Далее он видит, что сайт сгенерировал для неё уникальный урл - об этом есть текст
    def test_multiple_users_can_start_list_at_different_urls(self):
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element('id', 'id_new_item')
        inputbox.send_keys('Купить молоко')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Купить молоко')
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')

        # Теперь новый гражданин2 заходит на сайт. Никаких признаков старого гражданина нет.

        self.browser.quit()
        self.browser = webdriver.Firefox()

        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element('tag name', 'body').text
        self.assertNotIn('1: Купить молоко', page_text)
        self.assertNotIn('2: Купить кефир', page_text)

        # Гражданин2 начинает новый список, вводя новый элемент
        inputbox = self.browser.find_element('id', 'id_new_item')
        inputbox.send_keys('1: Купить творог')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Купить творог')

        # Гражданин2 получает уникальный урл
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # Опять таки, списка гражданина1 нет

        page_text = self.browser.find_element('tag name', 'body').text
        self.assertNotIn('1: Купить молоко', page_text)
        self.assertIn('1: Купить творог', page_text)

        self.fail('Закончить тест')
        # Она переходит на урл, список ещё там

        # Удовлетворённый гражданин ложится спать 
