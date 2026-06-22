# Marge two python dictionaries
dict1 = {1:100,2:200,"name": "Rahul",3:300}
dict2 = {4:400,5:500,"name": "Ram",6:600}
for i in dict2:
    dict1[i] = dict2[i]

print(dict1)