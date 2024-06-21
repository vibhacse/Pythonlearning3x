#tuple are immutable
tup1 = ("karthick","vivek","Bhar")
print(tup1)
print(len(tup1))

sample = {1,5,2,4} #SET: by default ASC order
print(sample)

sample1 = (10,20,30,40,15,50) #Tuples are immutable (not changable)
print(sample1)

a,b,c = (10,20,30)

t1 = (3,4,5)

print(a,b,c)

new_t = t1 + (50,)
print(new_t)

#convert tuple to list
listnew = list(t1)
listnew.append(123)
print(listnew)


