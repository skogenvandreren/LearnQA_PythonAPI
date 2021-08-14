import pytest


class TestLen:
    def test_len(self):
        phrase = input("Set a phrase less than 15 symbols: ")
        assert len(phrase) < 15, "Input phrase should be less than 15 symbols, " \
                                 f"actual phrase has {len(phrase)} symbols"