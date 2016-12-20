
def forRange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


#depth first search tree
class Node:
    def __init__(self, value):
        self.value = value
        self._children = []

    def __repr__(self):
        return 'Node{!r}'.format(self.value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()

class Countdown:
    def __init__(self, start):
        self.satrt = start

    def __iter__(self):
        n = self.satrt
        while n > 0:
            yield n
            n -= 1
    
    def __reversed__(self):
        n = 1
        while n <= self.satrt:
            yield n
            n += 1

if __name__ == "__main__":
    for n in forRange(0, 5, 0.5):
        print(n)
    print(list(forRange(0, 5, 0.5)))
    print('-'*30, end='\n')
    root =Node(0)
    child1= Node(1)
    child2= Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))
    for ch in root.depth_first():
        print(ch)
    print('-'*30, end='\n')
    for val in Countdown(10):
        print(val)
    print('\n');
    for val in reversed(Countdown(10)):
        print(val)