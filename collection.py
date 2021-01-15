from collections import Counter
from collections import namedtuple
from collections import defaultdict
from collections import deque
from collections import OrderedDict
a="aaaaabbbbcccdde"
my_counter = Counter(a)
print(my_counter)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())
# this returns a tuple with a list
print(my_counter.most_common(1))
#returns a list
print(list(my_counter.elements()))
# this will create a class with this fields
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt.x, pt.y)
ordered_dict = OrderedDict()
ordered_dict['a']=1
ordered_dict['b']=2
ordered_dict['c']=3
ordered_dict['d']=4
print(ordered_dict)
#default dict returns the specified value
d=defaultdict(int)
d['a']=1
d['b']=2
print(d['a'])
#deque is a double ended que
de= deque()
de.append(1)
de.append(2)
#add to the left
de.appendleft(3)
print(de)
de.popleft()
#de.clear() clears all the elements
#de.rotate(1) rotates the elements 1 pos to the right
print(de)
