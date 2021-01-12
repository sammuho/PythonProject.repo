
odds=frozenset([1,3,5,7,9])
evens=frozenset([0,2,4,6,8])
print(odds.union(evens))
print(odds.intersection(evens))
print(odds.difference(evens))
evens_copy=evens.copy()
print(evens_copy)
#a = "MY world is you"
#print(a)
#setA = {1,2,3,4,5,6,7,8,8}
#setB = {1,2,3,10,11,12}
#diff= setA.difference(setB)
#print(diff)
#diff=setA.symmetric_difference(setB)
#print(diff)
#setA.update(setB)
#print(setA)
#setA.difference_update(setB)
#print(setA)
#setA.symmetric_difference_update(setB)
#print(setA)
#setA.intersection_update(setB)
#print(setA)
#print(setA.issubset(setB))
#print(setB.issubset(setB))
#copying set
#setC = setB.copy()
#print(setC)
#b=frozenset([0,1,2,3,4,5])
#the following are not allowed
#b.add(5)
#b.remove(1)
#b.discard(1)
#b.clear()
#b.update([1,2,3])
#other set operations work
