#Set: removes duplicate

set1 = {10,20,30,10,40}
print(set1)

set2 = {50,60,70,80}
set2.add(20)
print(set2)

print(set1.union(set2))
print(set1.intersection(set2))

#Dictonary
student = {
    "name": "vivek",
    "PASSOUT": 2013,
    "Degree": "M. E",
}

print(student)
print(len(student))
print(student["Degree"])

#frozenset
x = frozenset({'name'})
y = frozenset({'age'})
dic = {x:'vivek', y:'34'}
print(dic)
