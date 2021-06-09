# type = "ProgrammingFiles"
# # programming files

# formats = [

# ]
# dic = {

# }

# for i in formats:
#     i = i.replace(".", "")
#     i = i.upper()
#     dic[i] = type
# print(dic)
# {
#     "name":
# },
# {
#     "name": ,
# },
# {
#    "name":
# },
import json
dic = {}
formats = json.load(open('pLE.json'))
for j in formats:
    print(j["name"])
    extensions = j["extensions"]
    for i in extensions:
        i = i.replace(".", "")
        i = i.upper()
        dic[i] = j["type"] + "/" + j["name"]
print(dic)
