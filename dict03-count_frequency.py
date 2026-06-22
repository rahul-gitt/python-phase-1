# count the frequency of each elements in a list using dictionaries
a = [1,1,1,1,2,2,2,2,3,4,4,4,4,5,5,5,5,5,0,0,0,0,6,6,6,6,6,7,8,9,9]
d1= {}
for i in a:
    if i in d1.keys():
        d1[i]+= 1
    else:
        d1[i] = 1

print(d1)
