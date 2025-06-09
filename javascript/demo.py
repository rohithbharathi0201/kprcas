a=10
b=20
c=30
if a > b and a > c:
    print ("a is greater")
elif b>a and b>c:
    print("b is greater")

else:
    print("c is greater ")
for i in range(1,6,2):
    print(i)

def add():
    print(30,50)
    add()

list={1,2,3,4,5}
for i in list:
    print(i)



tuple=(1,2,3,4,5);
for i in tuple:
    print(i)
    print (type(tuple))

dictionery = {"name":"bharathi","password":"123456"}
print(dictionery["name"])
print(type(dictionery))
for key in dictionery:
    print(dictionery[key])