li=[1,4,9,16,25,36,49,64,81,100]
for i in li:
    print(i)

li=(1,4,9,16,25,36,49,64,81,100)
for i in li:
    if(i==9):
        print(i,"is found at index",li.index(i))
        break
for i in range(1,11):   #start,stop
    print(i)
for i in range(2,200,2):   #start,stop,step/inecrement or decrement
    print(i)
    for i in range(100,0,-1):   
        print(i)
t1=int(input("Enter your first number : "))
for i in range(1,11):
    print(t1*i)
    # pass is also a reserved keyword in python which is used to create empty loops. It is also used for creating empty classes and functions.