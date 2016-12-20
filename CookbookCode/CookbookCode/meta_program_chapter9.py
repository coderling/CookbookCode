import time
from functools import wraps

def tiemThis(func):
    '''
    Decorator that reports then execution time.
    '''

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result
    return wrapper

@tiemThis
def countdown(n):
    '''
    coutn down
    '''
    while n > 0:
        n -= 1


#�Զ������Ե�װ����
from functools import wraps, partial
import logging

def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func

def logged(level, name=None, message=None):
    
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        @attach_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel

        @attach_wrapper(wrapper)
        def set_message(newMsg):
            nonlocal logmsg
            logmsg = newMsg

        return wrapper
    return decorate

@logged(logging.DEBUG)
def add(x, y):
    return x + y


import operator

class StructTupleMeta(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for n, name in enumerate(cls._fields):
            setattr(cls, name, property(operator.itemgetter(n)))

class StructTuple(tuple, metaclass=StructTupleMeta):
    _fields = []
    def __new__(cls, *args):
        if len(args) != len(cls._fields):
            raise ValueError('{} arguments required'.format(len(cls._fields)))
        return super().__new__(cls,args)

class Stock(StructTuple):
    _fields = ['name', 'shares', 'price']

if __name__ == '__main__':
    countdown(1000000)
    print('-' * 40)
    add(2,3)
    add.set_level(logging.WARNING)
    print('-' * 40)
    s = Stock('ACME', 50, 91.1)
    s.name
    print(s.name)
    print(dir(Stock))