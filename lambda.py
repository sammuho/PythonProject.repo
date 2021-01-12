# a lambda funtion that adds ten to the input argument
f=lambda x: x+10
val1 =f(5)
val2=f(100)
print(val1, val2)
#a lambda funtion that multiplies two inputs 
mul=lambda x,y:x*y
val3=mul(2,10)
val4=mul(7,5)
print(val3, val4)
#lambda inside a funtion
def myfunc(a):
    return lambda q:q*a
doubler=myfunc(2)
print(doubler(6))
tripler=myfunc(3)
print(tripler(6))
#custom sorting
points2D=[(1, 9),(4,1),(5,-3),(10,2)]
sorted_by_y= sorted(points2D, key=lambda x:x[1])
#x value of index 1
mylist= [-1, -4, -2, -3, 1, 2, 3, 4]
sorted_by_abs=sorted(mylist, key =lambda x: abs(x))
print(sorted_by_abs)