# collections={1,1,1,2,2,2,3,3,3,4,4,4,"Ali","Ali","umar"} #remove duplicate value/nmbrs
# print(collections)
# print(type(collections))
# print(len(collections))
# #Empty set and Methods of set
# empty=set()
# # print(empty)
# print(type(empty))
# empty.add(1)
# empty.add(2)
# empty.add(2)
# empty.add(3)
# empty.add(4)
# empty.add("ali")
# empty.remove(1)
# empty.add(("ali","umer","haha")) #tuple#
# empty.clear() #clear the set
# empty.pop() #remove random value in set
# print(empty)
#Intersection and union in sets
set1={1,2,3,4}
set2={5,1,6,3,4,8}
print(set1.union(set2))#donot change in original set
print(set1.intersection(set2)) #donot change in original set
