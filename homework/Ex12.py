import pytest
import requests


class TestHeaderValue:
    def test_header_value(self):
        url = "https://playground.learnqa.ru/api/homework_header"
        response = requests.get(url)
        headers = response.headers
        required_header = 'x-secret-homework-header'
        required_header_value = response.headers['x-secret-homework-header']
        assert 'x-secret-homework-header' in headers, f"Required header key ({required_header}) has not found "
        assert 'Some secret value' in required_header_value, f"Required header value ({required_header_value})" \
                                                             " has not found"
