#####################################################
## file name:class_chapter8
## create time:2016/6/26 21:30:47
## email:coderling@gmail.com
#####################################################


class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")

class SubPerson(Person):
    @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('setting name to', value)
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deletting name')
        super(SubPerson, SubPerson).name.__delete__(self)


#define self collections
import collections
import bisect

class SortedItems(collections.Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial is not None else []

    #必须实现的抽象函数
    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    #adding method
    def add(self, item):
        bisect.insort(self._items, item)

#代理类
class A:
    def spam(self, x):
        print("a.spam", x)
    def foo(self):
        print('a.foo')
    
class B:
    def __init__(self):
        self._a = A()

    def spam(self, x):
        print('b.spam', x)

    def bar(self):
        print('b.bar')

    def __getattr__(self, name):
        return getattr(self._a, name)

class C:
    __slots__ = ()

class D:
    pass

if __name__ == "__main__P":
    per = SubPerson('coderling')
    per.name
    print("-" * 40)
    items = SortedItems([5,1,3])
    print(list(items))
    print(items[0], items[-1])
    items.add(2)
    print(list(items))
    print("-" * 40)
    b = B()
    b.spam(1)
    b.foo()
    print("-" * 40)
    print(dir(C))
    print('dir D==')
    print(dir(D))



#访问者模式
class Node:
    pass

class UnaryOperator(Node):
    def __init__(self, operand):
        self.operand = operand

class BinaryOperator(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Add(BinaryOperator):
    pass

class Sub(BinaryOperator):
    pass

class Mul(BinaryOperator):
    pass

class Div(BinaryOperator):
    pass

class Negate(BinaryOperator):
    pass

class Number(Node):
    def __init__(self, value):
        self.value = value

class NodeVisitor:
    def visit(self, node):
        methname = 'visit_' + type(node).__name__
        meth = getattr(self, methname, Node)
        if meth is Node:
            meth = self.generic_visit
        return meth(node)

    def generic_visit(self, node):
        raise RuntimeError('No {} method'.format('visit_' + type(node).__name__))

class Evaluator(NodeVisitor):
    def visit_Number(self, node):
        return node.value

    def visit_Add(self, node):
        return self.visit(node.left) + self.visit(node.right)

    def visit_Sub(self, node):
        return self.visit(node.left) - self.visit(node.right)

    def visit_Mul(self, node):
        return self.visit(node.left) * self.visit(node.right)

    def visit_Div(self, node):
        return self.visit(node.left) / self.visit(node.right)

    def visit_Negate(self, node):
        return -node.operand


if __name__ == "__main__":
    print('访问者模式')
    e = Evaluator()
    print(e.visit(Number(4)))
    print(e.visit(Sub(Number(2), Number(3))))