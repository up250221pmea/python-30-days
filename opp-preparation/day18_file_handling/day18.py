# File Handling


# 1. Open and read a file

with open("notes.txt", "r") as file:
    content = file.read()

print(content)


# 2. Write in a file

with open("notes.txt", "w") as file:
    file.write("Learning Python")


# 3. Add content without deleting

with open("notes.txt", "a") as file:
    file.write("\nJava")


# 4. Save user input

language = input("Enter a programming language: ")

with open("languages.txt", "a") as file:
    file.write(language + "\n")


# 5. Read saved languages

with open("languages.txt", "r") as file:
    languages = file.read()

print(languages)


# 6. File path

with open("data/notes.txt", "r") as file:
    content = file.read()

print(content)


# 7. File not found

try:
    with open("config.txt", "r") as file:
        content = file.read()

    print(content)

except FileNotFoundError:
    print("File not found")


# This gives an error if the file does not exist:
# with open("something.txt", "r") as file:
#     content = file.read()


# Old way

file = open("notes.txt", "r")
content = file.read()
file.close()

print(content)