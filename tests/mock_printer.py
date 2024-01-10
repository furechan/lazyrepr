""" Mock Printer """

from io import StringIO

from contextlib import contextmanager


class MockPrinter:
    def __init__(self):
        self.buffer = StringIO()
        self.indent = 0

    def __str__(self):
        return self.buffer.getvalue()

    @classmethod
    def render(cls, obj):
        printer = cls()
        printer.pretty(obj)
        return str(printer)

    def pretty(self, obj):
        if hasattr(obj, "_repr_pretty_"):
            obj._repr_pretty_(self, False)
        else:
            self.text(repr(obj))

    def text(self, text):
        self.buffer.write(text)

    def breakable(self):
        self.buffer.write(" ")

    @contextmanager
    def group(self, indent, prefix="", suffix=""):
        self.indent += indent
        self.buffer.write(prefix)
        yield
        self.buffer.write(suffix)
        self.indent -= indent
