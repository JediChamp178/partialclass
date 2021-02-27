import functools
import collections


def partialcls(cls, *args, **kwds):
    'new class with partial application of the given arguments and keywords.\n'

    class NewCls(cls):
        __init__ = functools.partialmethod(cls.__init__, *args, **kwds)

    return NewCls
