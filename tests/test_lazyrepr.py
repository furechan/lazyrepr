""" lazyrepr tests """

from lazyrepr import ReprMixin
from mock_printer import MockPrinter


class MACD(ReprMixin):
    def __init__(self, short=12, long=26, signal=9, *, percent=False):
        self.short = short
        self.long = long
        self.signal = signal
        self.percent = percent


def test_repr():
    assert repr(MACD()) == "MACD(12, 26, 9)"
    assert repr(MACD(percent=True)) == "MACD(12, 26, 9, percent=True)"


def test_pretty():
    render = MockPrinter.render
    assert render(MACD()) == "MACD(12, 26, 9)"
    assert render(MACD(percent=True)) == "MACD(12, 26, 9, percent=True)"
