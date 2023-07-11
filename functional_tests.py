from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    '''Tect нового посетителя'''
    
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()
    
    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_layer(self):
        '''Можно ли начать список и получить его позже'''
        # Некий гражданин слышал про новое крутое приложение со списком дел. Он хочет оценить его домашнюю страницу.
        self.browser.get('http://localhost:8000')

        # Он видит, что заголовок и шапка страницы говорят о списках дел
        self.assertIn('To-Do', self.browser.title)
        self.fail('Закончить тест!')

        # Ему сразу же предлагается ввести элемент списка (дело)

        # Она набирает в текстовом поле "Купить молоко"

        # Когда она нажимает enter страница обновляется и теперь страницу содержит 1: "Купить молоко"

        # Текстовое поле по прежнему предлагает ей добавить ещё один элемент списка. Она вводит "Купить кефир"

        # Страница снова обновляется и показывает оба элемента её списка

        # Гражданину интересно, запомнит ли сайт её список. Далее он видит, что сайт сгенерировал для неё уникальный урл - об этом есть текст

        # Она переходит на урл, список ещё там

        # Удовлетворённый гражданин ложится спать 


if __name__ == '__main__':
    unittest.main(warnings='ignore')