# dictionary and sets

# dict = {
#     "name" : "ravi",
#     "age" : 20,
#     "marks" : [98, 97, 95]
# }
# dict["age"] = 21
# dict["surname"] = "singh"
# print(dict)
# print(dict["age"])

# student = {
#     "name" : "ravi",
#     "subject" : {
#         "phy" : 97,
#         "chem" : 98,
#         "bio" : 94
#     }
# }
# print(student)
# print(student["subject"])
# print(student["subject"]["phy"])

# dict = {
#     "name" : "ravi",
#     "age" : 20,
#     "marks" : [98, 97, 95]
# }
# dict2 = {
#     "city" : "jaipur",
#     "state" : "rajasthan"
# }
# print(dict)
# print(dict.keys())
# print(list(dict.keys()))
# print(dict.values())
# print(dict.items())

# print(dict["name2"]) #ERROR IN THIS CASE CODDE EXECUTION STOPS 
# print(dict.get("name2")) #CORRECT WAY TO USE VALUES 

# dict.update({"sub" : "phy"})
# dict.update(dict2)
# print(dict)

#sets
# collection = {1, 2, 3, 4, "hello", "world", 2}
# print(type(collection))
# print(len(collection))
# collection.add(99)
# collection.remove(4)
# collection.remove(80)
# collection.clear()
# val = collection.pop()
# print(collection)
# print(val)

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# print(set1.union(set2))
# print(set1.intersection(set2))

# dict = {}
# dict.update({"table" : ["a piece of furniture", "list of facts and figs"], "cat" : "a small animal"})
# print(dict)

# dict = {}
# mark1 = int(input("enter marks of phy : "))
# mark2 = int(input("enter marks of chem : "))
# mark3 = int(input("enter marks of bio : "))
# dict.update({"phy" : mark1, "chem" : mark2, "bio" : mark3})
# print(dict)

# set = {int(9), float(9.0)}
set = {9, "9.0"} #CORRECT
# a= int(9)
# b= float(9.0)
# print(a, b)
# set = {a, b}
print(set)