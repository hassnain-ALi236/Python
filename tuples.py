# tuples is also almost same for lists but it is immuatable(cannot change(list can be change their index))
data=(939,"Hassnain",827,"Umair",1026,"Talha")
print(data)
# data[0]=900   cannot apply in tuple bcz it is immuatable 
# print(data)
# print(data.index(827))
# data.inddex show the index value
# print(data.count("Umair"))
# print(any(data))   
# any(data) check tuples is iterable or not
# print(len(data))
# print(id(data))  
# a list can be convert to tuple
# li=[1,3,4,5,6]
# tup=tuple(li)
# print(type(tup))
grade=('A',"B",'C')
add=data+grade
print(add)
# concatination only allowed in tuples not in list  
marks= (985, 939, 827, 939, 1016, 812)
print(sum(marks))
# sum fun only allowed for numericals values