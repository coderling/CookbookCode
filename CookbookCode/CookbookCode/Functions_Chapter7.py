#####################################################
## file name:Functions_Chapter7
## create time:2016/6/19 21:41:57
## email:coderling@gmail.com
#####################################################

def anyarges(*args, **kwargs):
    print(args)
    print(kwargs)


#装饰器
def apply_async(func, args, *, callback):
    result = func(*args)
    callback(result)

def add(x, y):
    return x + y

def print_result(result):
    print('Got:', result)

from queue import Queue
from functools import wraps

class Async:
    def __init__(self, func, args):
        self.func = func
        self.args = args

def inlined_asnc(func):
    @wraps(func)
    def wrapper(*args):
        f = func(*args)
        result_queue = Queue()
        result_queue.put(None)
        while True:
            result = result_queue.get()
            try:
                a = f.send(result)
                apply_async(a.func, a.args, callback=result_queue.put)
            except StopIteration:
                break
    return wrapper

@inlined_asnc
def testWrapper():
    r = yield Async(add, (2, 3))
    print(r)
    r = yield Async(add, ('hello', 'world'))
    print(r)
    for n in range(10):
        r = yield Async(add, (n,n))
        print(r)
    print('Goodbye')


#访问闭包中定义的变量
import sys
class ClosureInstance:
    def __init__(self, locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals

        self.__dict__.update((key, value) for key, value in locals.items() 
                             if callable(value))
        def __len__(self):
            return self.__dict__['__len__']()

def Stack():
    items = []
    def push(item):
        items.append(item)

    def pop():
        return items.pop()

    def __len__():
        return len(items)

    return ClosureInstance()

if __name__ == "__main__":
    anyarges(1,2,3,4,5, aa = 0, bb = 1)
    print('-'*40)
    #a = testWrapper()
    import multiprocessing
    pool = multiprocessing.Pool()
    apply_async = pool.apply_async

    testWrapper()

    print('-'*40)
    
    s = Stack()
    s.push(10) 
    s.push(20)
    s.push('aa')
    len(s)