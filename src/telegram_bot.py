import telebot
import requests

token = "1896816293:AAE04aQjnZkKwq6sFPpzuiK7S1mtnkmSW0k"
chat_id = "153513539"
sender_chat_id = "1001515574051"


def telegram_bot_send_text(token, chat_id, message):
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=Markdown&text={message}'
    response = requests.get(url)
    return response.json()


# resp = telegram_bot_send_text(token, chat_id, "Hello")


# bot = telebot.TeleBot('1896816293:AAE04aQjnZkKwq6sFPpzuiK7S1mtnkmSW0k')

# def start():
#     bot = telebot.TeleBot("1896816293:AAE04aQjnZkKwq6sFPpzuiK7S1mtnkmSW0k")
#     bot.send_message("1001515574051", "Hi")
#
#
# def test_send():
#     start()

def pytest_session_finish(session, exitstatus):
    if exitstatus is ExitCode.TESTS_FAILED:
        failed_tests = []
        for item in session.items:
            if item.rep_call.failed:
                failed_tests.append(item.name)
        failed_tests_joined = "\n".join(map(lambda failed_case: F"> {failed_case}", failed_tests))
        message = \
            F"Tests failed/collected: {session.testsfailed}/{session.testscollected}\nFails:\n{failed_tests_joined}"
#         bot = telebot.TeleBot("1896816293:AAE04aQjnZkKwq6sFPpzuiK7S1mtnkmSW0k")
#         bot.send_message("1001515574051", message)
