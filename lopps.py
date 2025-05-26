"""add= 0
for i in range(1,7):
    add= i+add
print(add)


file1 = open('FindByIdXPathDemo.txt')
print(file1.read())
while file1!="":
    print(file1)
    file1=file1.read()
"""

#exception handling

try:
    with open("FindByIdXPathDemo.txt", 'r') as read:
        read.read()

except Exception as e:
    print(e)

finally:
    print("okk")
