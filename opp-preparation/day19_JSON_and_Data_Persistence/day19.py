# JSON and Data Persistence

import json


# 1. JSON

# JSON means JavaScript Object Notation.
# It is a format used to store structured data.
# It looks very similar to a Python dictionary.

user = {
    "name": "Eliut",
    "career": "Software Development",
    "active": True
}

# In a JSON file, it would look similar to this:
#
# {
#     "name": "Eliut",
#     "career": "Software Development",
#     "active": true
# }
#
# JSON has its own syntax.
#
# Python        JSON
# True          true
# False         false
# None          null


# 2. json.dump()

# json.dump() is used to save Python data
# inside a JSON file.

profile = {
    "name": "Eliut",
    "language": "Python",
    "level": "Beginner"
}

with open("profile.json", "w") as file:
    json.dump(profile, file, indent=4)

# json.dump(data, file)
#
# profile -> the data we want to save
# file    -> the file where the data will be stored
#
# indent=4 makes the JSON file easier to read.


# 3. json.load()

# json.load() is used to read data from a JSON file
# and convert it back into Python data.

with open("profile.json", "r") as file:
    profile_data = json.load(file)

print(profile_data)

# In this case, profile_data becomes a dictionary again.

print(type(profile_data))

# Output:
# <class 'dict'>


# 4. Accessing loaded data

# Since json.load() converted the JSON data
# into a dictionary, we can use it normally.

print(profile_data["name"])
print(profile_data["language"])
print(profile_data["level"])


# 5. Dictionaries and JSON

student = {
    "name": "Eliut",
    "subjects": ["Programming", "Databases", "OOP"],
    "active": True,
    "grade": None
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

# Common conversions:
#
# Python       JSON
# dict         object
# list         array
# str          string
# int/float    number
# True         true
# False        false
# None         null


# 6. Saving lists

# JSON can also store lists, not only dictionaries.

languages = [
    "Python",
    "Java",
    "C#"
]

with open("languages.json", "w") as file:
    json.dump(languages, file, indent=4)

# We can load the list again using json.load().

with open("languages.json", "r") as file:
    saved_languages = json.load(file)

print(saved_languages)

for language in saved_languages:
    print(language)


# 7. Data Persistence

# Data persistence means that the information
# can still exist after the program finishes.
#
# Example:
#
# score = 100
#
# If score only exists inside the program,
# the value is lost when the program closes.
#
# If we save it in a JSON file,
# we can recover it later.

progress = {
    "course": "Python 30 Days",
    "completed_days": 18
}

with open("progress.json", "w") as file:
    json.dump(progress, file, indent=4)


# 8. Load, Modify and Save

# A common pattern when working with stored data is:
#
# LOAD -> MODIFY -> SAVE

with open("progress.json", "r") as file:
    progress = json.load(file)

progress["completed_days"] += 1

with open("progress.json", "w") as file:
    json.dump(progress, file, indent=4)

print(progress)


# 9. JSON + Exception Handling

# If we try to open a file that does not exist,
# Python raises a FileNotFoundError.
#
# We can combine JSON with try / except.

try:
    with open("settings.json", "r") as file:
        settings = json.load(file)

    print(settings)

except FileNotFoundError:
    print("The settings file does not exist.")


# Summary

# JSON:
# A format used to store structured data.

# json.dump()
# Saves Python data into a JSON file.
# Python -> JSON

# json.load()
# Reads data from a JSON file
# and converts it into Python data.
# JSON -> Python

# Data Persistence:
# Saving information so it can still be used
# after the program finishes.

# Common pattern:
#
# 1. Load
# 2. Modify
# 3. Save