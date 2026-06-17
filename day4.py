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

dict = {
    "name" : "ravi",
    "age" : 20,
    "marks" : [98, 97, 95]
}

print(dict)
print(dict.keys())
print(list(dict.keys()))
print(dict.values())
print(dict.items())