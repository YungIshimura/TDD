from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase


class NewVisitorTest(LiveServerTestCase):
    '''Tect нового посетителя'''
    
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()
    
    def tearDown(self) -> None:
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        '''Подтверждение строки в таблице списка'''
        table = self.browser.find_element('id', 'id_list_table')
        rows = table.find_elements('tag name', 'tr')
        self.assertIn(row_text, [row.text for row in rows])

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
        self.check_for_row_in_list_table('1: Купить молоко')

        table = self.browser.find_element('id', 'id_list_table')
        rows = table.find_elements('tag name', 'tr')
        self.assertIn('1: Купить молоко', [row.text for row in rows])
        # Текстовое поле по прежнему предлагает ей добавить ещё один элемент списка. Она вводит "Купить кефир"
        
        inputbox = self.browser.find_element('id', 'id_new_item')
        inputbox.send_keys('Купить кефир')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

    
        # Страница снова обновляется и показывает оба элемента её списка
        self.check_for_row_in_list_table('1: Купить молоко')
        self.check_for_row_in_list_table('2: Купить кефир')
        # Гражданину интересно, запомнит ли сайт её список. Далее он видит, что сайт сгенерировал для неё уникальный урл - об этом есть текст
        self.fail('Закончить тест')
        # Она переходит на урл, список ещё там

        # Удовлетворённый гражданин ложится спать 
