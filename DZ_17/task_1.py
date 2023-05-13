# 1. Створити клас Bot з атрибутом name та методами say_name та send_message.
# send_message має приймати параметри self і message і має друкувати message.
# Метод say_name має друкувати значення атрибуту name.


class Bot:
    def __init__(self, name):
        self.name = name

    def say_name(self):
        return self.name

    def send_message(self, message):
        print(message)


some_bot = Bot("Lord of the White rabbits")

print(some_bot.say_name())

some_bot.send_message("Hello! How did you get here?")


# 2. Створити клас TelegramBot, який має бути унаслідуваний від Bot та має містити:
# власні атрибути url, chat_id (None за замовчуванням)
# методи send_message, set_url та set_chat_id.
# Ці методи, крім self,  мають приймати 1 параметр (url та chat_id відповідно)
# та присвоювати значення цього параметру атрибутам url та chat_id відповідно.
# Також TelegramBot має перевизначити метод send_message – друкувати значення параметру
# message з будь-яким допоміжним текстом. Цей текст також має містити в собі значення url та chat_id


class TelegramBot(Bot):
    def __init__(self, name):
        super().__init__(name)
        self.url = None
        self.chat_id = None

    def set_url(self, url):
        self.url = url

    def chat_id(self, chat_id):
        self.chat_id = chat_id

    def send_message(self, message):
        print(f"{telegram_bot.say_name()} says {message} Come to our chat {self.chat_id} using {self.url}")


telegram_bot = TelegramBot("White rabbit's girlfriend")

print(telegram_bot.say_name())

telegram_bot.send_message('Hello!')

telegram_bot.chat_id = 1

telegram_bot.send_message("Hello!")
