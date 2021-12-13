from States import State_Machine

class Handler_message:

    def __init__(self):
        self.storage = {}

    def state(self, chat_id):
        try:
            return self.storage[chat_id]['state'].state
        except KeyError:
            self.storage.update({
                chat_id: {
                    'state': State_Machine(),
                    'size': None,
                    'payment': None,
                }
            })
            return self.storage[chat_id]['state'].state


    def get_answer(self, chat_id, message):
        text = message.lower()
        if self.state(chat_id) == 'start_bot' and text == '/start':
            self.storage[chat_id]['state'].next_state()
            return 'Какую вы хотите пиццу? Большую или маленькую?'

        elif text == '/reset':
            self.storage[chat_id]['state'].cancel()
            return 'Для заказа пиццы нажмите /start.'

        elif self.state(chat_id) == 'pizza_size':
            if text in ['большую', 'маленькую']:
                self.storage[chat_id]['size'] = text
                self.storage[chat_id]['state'].next_state()
                return 'Как вы будете платить?'
            else:
                return 'Выберите размер пиццы: большую или маленькую?'

        elif self.state(chat_id) == 'payment_method':
            if text in ['наличкой', 'картой']:
                self.storage[chat_id]['payment'] = text
                self.storage[chat_id]['state'].next_state()
                return f"Вы хотите {self.storage[chat_id]['size']} пиццу, оплата - {self.storage[chat_id]['payment']}?"
            else:
                return 'Введите способ оплаты: наличкой или картой?'

        elif self.state(chat_id) == 'checking':
            if text == 'да':
                self.storage[chat_id]['state'].next_state()
                return 'Спасибо за заказ'
            elif text == 'нет':
                self.storage[chat_id]['state'].cancel()
                return 'Начните заказ заново с команды /start.'
            else:
                return f"Вы выбрали {self.storage[chat_id]['size']} пиццу, " \
                       f"оплата - {self.storage[chat_id]['payment']} верно?: Да или Нет."

        return 'Сделайте заказ с помощью команды /start.'