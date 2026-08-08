# x = 10
# x += 5

# print(x * 2)


x = [1, 2, 3, 4]

y = x

y.append(5)

x = x.insert(1,10)




print(x)
print(y) 

# this program demonstrates the concept of mutable objects. 
# When we assign y = x, we are not creating a new list, but rather making y refer to the same list object as x.  