"""a=10
b=2
print("multiply",a*b)
print("plus",a+b)
print("minus",a-b)
print("divide",a/b)
print("po",a**b)

a=input("enter value of a")
b=input("enter value of b")
print(int(a)+int(b))

a="ayusshhh"
print(len(a))
print(a[-4:-2])

import time

timestamp = time.strftime('%H:%M')
print(timestamp)
#time_hour=timestamp.split(":")[0]
#print(time_hour)

if(timestamp >= ('12') and timestamp<=('16')):
    print("Good afternoon")
elif(timestamp>=('16') and timestamp<=('22')):
    print("good eveng")
elif(timestamp>=('22') or timestamp<=('03')):
    print(("good night"))
else:
    print("gd mrng")


#list examples
a, b, c =50, 10, 5.6
print("value of c:",type(c),c,"hello")

value=[10, 2.51, "helluu", 0.5]
hi= "kaise of kya lre ho"
print(len(value))
print(len(hi))
value.insert(3,"ayush")
print(value)


#dictionaryyy example
a= {1:"helluu",2:"ayush"}
print(a[1])
print(a[2])


#how to insert in empty dictionary
dict ={}

dict={"name":"ayush"}
dict={"last name":"srivastav"}
print(dict)
"""