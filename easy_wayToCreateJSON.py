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

# // from ProgrammingLanguagesAndTheirExtensions.json

# {
#    "name": "Jasmin",
#    "type": "programming",
#    "extensions": [".j"]
# },

# //  FileType.json

# "MP3": "Songs",
import json
dic = {}
formats = json.load(open('ProgrammingLanguagesAndTheirExtensions.json'))
for j in formats:
    extensions = j["extensions"]
    for i in extensions:
        i = i.replace(".", "")
        i = i.upper()
        dic[i] = j["type"] + "/" + j["name"]

# converting dictionary to json object
json_object = json.dumps(dic, indent=4)

# Writing to FileTypes.json

# with open("sample.json", "w") as outfile:
#     outfile.write("FileTypes.json")
print(dic)
