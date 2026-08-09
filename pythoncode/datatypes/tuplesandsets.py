# tuples are mutable 

a = (1,2,3,4,5,6,6,6,6,7,7)

user_name = ("admin", "Guest", "kapil")

print(a[1])
print(a[1:4])

# set are unordered and unindexed

s = {1,2,3,4,5,6,6,6,7,7,8,8}
print(s)

l = [1,2,3,4,5,6,7,7,7,8,9,9]
print(l)

l = set(l)
print(l)

l = list(l)
print(l)