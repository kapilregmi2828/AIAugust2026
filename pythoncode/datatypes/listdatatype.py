a = [1, 2, 3, 4, 5, "Kapil", 10.5, 2j,True]
b = [1,1,1,2,2,2,3,3,3]

c = [10,20,30,40,50] # indexed as 0,1,2,3,4 or -5,-4,-3,-2,-1

print(c)
print(c[0])
print(c[4])
print(c[0:3])
print(c[-4])

# adding data to the list: append, insert, extend

c.append(60)
print(c)

c.insert(2,25)
print(c)

b.extend(a)
print(b)

# deleting data from the list: remove, pop, clear, del

d = [10,20,30,40,50,30,30]
print(d)

d.remove(30) # removes first occurence of 30
print(d)

d.pop(5)#used to delete indexed element from the list
print(d)

d.clear() # clear() method removes all the ekelements from the list
print(d)

del d # deletes the entire list 

# sorting list 

e = [10,20,40,15,1,50,45, 30]
print(e)
e.sort()
print(e)

# sorting in descending order

e.sort(reverse=True)
print(e)



