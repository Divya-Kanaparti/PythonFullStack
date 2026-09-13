import copy
a=[1,2,3]
print(a,id(a))
b=a
c=a.copy()     #shallow copy->doesnt share adress but have same data
print(b,id(b))    #a,b points to same adress
b[0]=11
print(a,b)
a1=[1,2,3,[4,5]]
print(a1,id(a1))
b1=copy.deepcopy(a1)   
print(b1,id(b1))
print(id(a1[3]))
print(id(b1[3]))
#eg:3
x=[1,2,3]
y=[11,22,33]
print(list(zip(a,b)))
for index,element in enumerate([a,b]):
    print(index,element)
#eg:4
d={}
for i in range(2):
    id=int(input("enter id:"))
    name=input("enter name:")
    d[id]=id
    d[name]=name
print(d)
#eg:5
n=int(input("enter no:"))
l=list(map(int,input().split()))[:n]
print(sum(l))
print(l)