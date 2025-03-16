""" lazyrepr tests """

from lazyrepr import ReprMixin
from mock_printer import MockPrinter


class Foo(ReprMixin):
    def __init__(self, name="foo", *, flag: bool = False):
        self.name = name
        self.flag = flag


def test_repr():
    assert repr(Foo()) == "Foo('foo')"
    assert repr(Foo("bar")) == "Foo('bar')"
    assert repr(Foo(flag=True)) == "Foo('foo', flag=True)"
    assert repr(Foo.__new__(Foo)) == "Foo(?, flag=?)"


def test_pretty():
    pprint = MockPrinter.render
    assert pprint(Foo()) == "Foo('foo')"
