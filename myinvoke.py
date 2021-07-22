# content of myinvoke.py
import pytest
import sys

from _pytest.config import ExitCode
from telebot.apihelper import session

from src.telegram_bot import telegram_bot_send_text


class MyPlugin:
    def pytest_sessionfinish(self):
        print("*** test run reporting finishing")

        # token = "1896816293:AAE04aQjnZkKwq6sFPpzuiK7S1mtnkmSW0k"
        # chat_id = "153513539"
        #
        # if ExitCode.TESTS_FAILED:
        #     failed_tests = []
        #     for item in session.items:
        #         if item.rep_call.failed:
        #             failed_tests.append(item.name)
        #     failed_tests_joined = "\n".join(map(lambda failed_case: F"> {failed_case}", failed_tests))
        #     message = \
        #         F"Tests failed/collected: {session.testsfailed}/{session.testscollected}\nFails:\n{failed_tests_joined}"
        #     telegram_bot_send_text(token, chat_id, message)


if __name__ == "__main__":
    sys.exit(pytest.main(["-qq"], plugins=[MyPlugin()]))
