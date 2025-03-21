# Python utilities for concise object representation

This library provides utilities to implement the `__repr__`
and ipython `_repr_pretty_` methods to represent objects in a concise manner.
The implementation is based on the class `__init__` method signature,
and will differentiate between positional and optional parameters
in order to make the representation as succinct as possible.

These methods are intended to be used on simple classes that map all their constructor arguments to attributes. Also note that `dataclasses` already implement a similar `__repr__` method by default.


## Usage

To add a basic representation to a class you can overrides its `__repr__` method with `lazy_repr` as follows:

```python
from lazyrepr import lazy_repr

class MyClass:
    __repr__ = lazy_repr
    ...
```

To provide both `__repr__` and ipython `_repr_pretty_` for a class just inherit from `ReprMixin`

```python
from lazyrepr import ReprMixin

class MyList(ReprMixin):
    def __init__(self, item=()):
        self.items = list(items)

lst = MyList(range(3))
print(lst)  # >>> MyList([0, 1, 2])
```

## Examples

Examples notebooks are in the `extras` folder.

## Installation

You can install this package with `pip`.

```console
pip install lazyrepr
```

## Related Projects and Resources

- [easyrepr](https://github.com/chrisbouchard/easyrepr)
Python decorator to automatically generate repr strings 
