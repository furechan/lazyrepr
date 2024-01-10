# Python mixin class for concise object representation

This library offers a mixin class `ReprMixin` that implements the `__repr__`
and `_repr_pretty_` methods to represent objects in a concise way.
The implementation is based on the class `__init__` method signature,
and will consider whether its parameters are positional or optional
to construct a representation as succinct as possible.
Positional arguments are represented as values only and 
optional arguments are included only when different from their default value.

Please note this is intended to be used on lightweight classes that map arguments to attributes.
Also it will not work with dataclasses that override the `__repr__` method.


## Usage

```python
from lazyrepr import ReprMixin

class MACD(ReprMixin):
    def __init__(self, short=12, long=26, signal=9, *, percent=False):
        self.short = short
        self.long = long
        self.signal = signal
        self.percent = percent

obj = MACD()
print(obj)  # >>> MACD(12, 26, 9)
```

## Examples

Examples notebooks are in the `extras` folder.

## Installation

You can install this package with `pip`.

```console
pip install git+ssh://git@github.com/furechan/lazyrepr.git
```

## Related Projects

- [easyrepr](https://github.com/chrisbouchard/easyrepr)
Python decorator to automatically generate repr strings 
