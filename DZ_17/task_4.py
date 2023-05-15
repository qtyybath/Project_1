# 5. Створити клас Bot та TelegramBot із першого завдання за допомогою функції type


class Bot:
    name = "say_name"
    message = "send_message"
    Bot_type = type("Bot", (), {"name": "say_name", "message": "send_message"})


Bot.name = "Lord of the White rabbits"
Bot.message = "Hello! How did you get here?"
print(f"{Bot.name} says: {Bot.message} ")


class TelegramBot:
    set_url = "url"
    chat_id = "id"
    Tel_type = type("TelegramBot", (Bot,), {"set_url": "url", "chat_id": "id"})


TelegramBot.name = "White rabbit's girlfriend"
TelegramBot.message = 'Hello!'
TelegramBot.set_url = None
TelegramBot.chat_id = 1
print(f"{TelegramBot.name} says: {TelegramBot.message} Come to our chat {TelegramBot.chat_id} using {TelegramBot.set_url}")
