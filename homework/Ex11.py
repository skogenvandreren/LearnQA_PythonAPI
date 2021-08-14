import pytest
import requests


class TestCookieFetch:
    def test_cookie_fetch(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"
        session = requests.Session()
        response = session.get(url)
        session_cookie = session.cookies.get_dict()
        assert 'HomeWork' in session_cookie and session_cookie is not None, "Method doesnt work, can`t fetch cookie " \
                                                                            f"from response, (actual cookie is {session_cookie}) "
        return session_cookie
