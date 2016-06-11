
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

#find common in too dict or diff
def commonOrDiff():
    print('-'*30, end='\n')
    a = {'x':1, 'y':2, 'z':3}
    b = {'w':10, 'x':11, 'y':2}
    #common keys
    print(a.keys() & b.keys())
    #diff keys
    print(a.keys() - b.keys())
    #common items
    print(a.items() & b.items())

if __name__ == "__main__":
    print('-'*30, end='\n')
    testDefaultdict()
    commonOrDiff()

#去除重复元素，并且保持集合元素顺序不变
def dedupe(items, key=None):
    seen = set()
    for item in items:
        #如果item不是可哈希的，那么通过key给定的函数把他转换成可哈希
        val = item if key is None else key(item)
        if item not in seen:
            yield item
            seen.add(item)

def deleteCommon():
    items = [1, 5, 2, 1, 9, 1, 5, 10]
    a = list(dedupe(items))
    print(a)

if __name__ == "__main__":
    print('-'*30, end='\n')
    deleteCommon()


#Counter use
from collections import Counter
def counterUse():
    words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the'
             ,'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
             'eyes', "don't", 'look', 'around', 'the']
    words_counter = Counter(words)
    print(words_counter)
    print("most_common = >", words_counter.most_common(3))
    #update
    morewords = ['why', 'are', 'you' 'not', 'looking', 'in', 'my', 'eyes']
    words_counter.update(morewords)
    print("update=>", words_counter)
    #math 
    a = Counter(words)
    b = Counter(morewords)
    print("add=>", a + b)
    print("dec=>", b - a)#小于等于0的Count不在Counter中去掉。


#groupby 
from operator import itemgetter
from itertools import groupby

def groupBy():
    rows = [
            {'address': '5412 NCLARK','date':'07/01/2012'},
            {'address': '5148 NCLARK','date':'07/04/2012'},
            {'address': '5800 E58TH','date':'07/02/2012'},
            {'address': '2122 NCLARK','date':'07/03/2012'},
            {'address': '5645 NRAVENSWOOD', 'date': '07/02/2012'},
            {'address': '1060 WADDISON','date': '07/02/2012'},
            {'address': '4801 NBROADWAY','date': '07/01/2012'},
            {'address': '1039 WGRANVILLE', 'date': '07/04/2012'},
          ]
    #sort row first
    rows.sort(key=itemgetter('date'))
    #iterate in groups
    for date, items in groupby(rows, key=itemgetter('date')):
        print(date)
        for i in items:
            print(' ', i)


#sub set make
def makeSubSet():
    prices= {
        'ACME':45.23,
        'AAPL':612.78,
        'IBM':205.55,
        'HPQ':37.20,
        'FB': 10.75
        }
    #make a dict of all prices over 200
    p1 = {key: value for key, value in prices.items() if value > 200}
    #make a dict of tech stocks
    tech_names= {'AAPL', 'IBM', 'HPQ', 'MSFT'}
    p2 = {key: value for key, value in prices.items() if key in tech_names}

    print("p1=>", p1)
    print("p2=>", p2);

    #also can use dict(),but slower
    p3 = dict((key, value) for key, value in prices.items() if value > 200)
    print("p3=>", p3)

#namedtuple
from collections import namedtuple

def useNametuple():
    Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
    sub = Subscriber('jonesy@example.com', '2012-10-19')
    print("sub=>", sub)
    print(sub.addr)
    print(sub.joined)

if __name__ == "__main__":
    print('-'*30, end='\n')
    counterUse()
    print('-'*30, end='\n')
    groupBy()
    print('-'*30, end='\n')
    makeSubSet()
    print('-'*30, end='\n')
    useNametuple()

