import unittest
from handler_message import Handler_message
from States import State_Machine

class TestRequests(unittest.TestCase):

    def setUp(self):
        self.handler = Handler_message()
        self.chat_id = '1111'
        self.handler.state(self.chat_id)
        self.storage = self.handler.storage

    def test_start_bot(self):
        self.storage[self.chat_id]['state'] = State_Machine('start_bot')
        self.assertEqual(self.handler.get_answer(self.chat_id, '/start'),
                         'Какую вы хотите пиццу? Большую или маленькую?')

    def test_incorrect_pizza_size(self):
        self.storage[self.chat_id]['state'] = State_Machine('pizza_size')
        self.assertEqual(self.handler.get_answer(self.chat_id, 'Не подходящее сообщение'),
                         'Выберите размер пиццы: большую или маленькую?')

    def test_correct_pizza_size(self):
        self.storage[self.chat_id]['state'] = State_Machine('pizza_size')
        self.assertEqual(self.handler.get_answer(self.chat_id, 'маленькую'), 'Как вы будете платить?')

    def test_incorrect_payment_method(self):
        self.storage[self.chat_id]['state'] = State_Machine('payment_method')
        self.assertEqual(self.handler.get_answer(self.chat_id, 'Неподходящее сообщение'),
                         'Введите способ оплаты: наличкой или картой?')

    def test_correct_payment_method(self):
        self.storage[self.chat_id]['state'] = State_Machine('payment_method')
        self.assertEqual(self.handler.get_answer(self.chat_id, 'картой'),
                         f"Вы хотите {self.storage[self.chat_id]['size']} пиццу, "
                         f"оплата - {self.storage[self.chat_id]['payment']}?")

    def test_incorrect_checking(self):
        self.storage[self.chat_id]['state'] = State_Machine('checking')
        self.assertEqual(self.handler.get_answer(self.chat_id, 'Неподходящее сообщение'),
                         f"Вы выбрали {self.storage[self.chat_id]['size']} пиццу, "
                         f"оплата - {self.storage[self.chat_id]['payment']} верно?: Да или Нет.")

    def test_negative_checking(self):
        self.storage[self.chat_id]['state'] = State_Machine('checking')
        self.assertEqual(self.handler.get_answer(self.chat_id, 'нет'), 'Начните заказ заново с команды /start.')

    def test_positive_checking(self):
        self.storage[self.chat_id]['state'] = State_Machine('checking')
        self.assertEqual(self.handler.get_answer(self.chat_id, 'да'),'Спасибо за заказ')

    def test_reset(self):
        self.assertEqual(self.handler.get_answer(self.chat_id, '/reset'), 'Для заказа пиццы нажмите /start.')

    def test_incorrect_start_bot(self):
        self.storage[self.chat_id]['state'] = State_Machine('start_bot')
        self.assertEqual(self.handler.get_answer(self.chat_id, 'Любое сообщение'),
                         'Сделайте заказ с помощью команды /start.')

if __name__ == "__main__":
    unittest.main()