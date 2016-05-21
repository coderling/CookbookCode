
#conllections.deque sample
from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

#find max n or min n sulution
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
if __name__ == "__main__":
    print('-'*30, end='\n')
    print(heapq.nlargest(3, nums))
    print(heapq.nsmallest(3, nums))
    #use key
    #use lambda to handle every elements. get then nlargest in result.
    print(heapq.nlargest(3, nums, key=lambda va: -va))
    #then heapq is smallest heap.

#the PriorityQueue implement by heapq
class Item():

    def __init__(self, name):
        self._name = name

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        #可迭代结构之间比较大小，从左到右比较遇到不相等，返回结果。
        #但未必结构内素有元素都是可比较的，增加index，由于index一定不一样，所有肯定会有结果。
        #_index小时先插入的元素。
        heapq.heappush(self._queue, (-priority, self._index, item))
        print(self._queue)
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

if __name__ == "__main__":
    print('-'*30, end='\n')
    q = PriorityQueue()
    q.push('foo', 1)
    q.push('bar', 5)
    q.push('spam', 4)
    q.push('grok', 1)
    print(q.pop(),end='\n')
    print(q.pop(),end='\n')
    print(q.pop(),end='\n')
    print(q.pop(),end='\n')

    
    if (3, Item('a')) < (5, Item('b')):
        print("true")

#dict 字典
#use defaultdict make code sample 
from collections import defaultdict
def testDefaultdict():
    d = {}
    #when add a elemts
    pairs = [('a','1'), ('b','2'), ('c','3')]
    for key, value in pairs:
        if key not in d:
            d[key] = []
        d[key].append(value)
    print("d => ", d)

    b = defaultdict(list)
    for key, value in pairs:
        b[key].append(value)
    print("b => ", d)

if __name__ == "__main__":
    print('-'*30, end='\n')
    testDefaultdict()