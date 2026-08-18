
# ! Mutability and References


# 1. Mutable and immutable objects

numbers = [1, 2, 3]
numbers.append(4)

# The same list is modified
# numbers -> [1, 2, 3, 4]

name = "eliut"
name = name.upper()

# Strings are immutable, so a new value is created
print(numbers)
print(name)


# 2. References

a = [10, 20, 30]
b = a

# Both variables point to the same list
#
# a ───┐
#      ↓
# [10, 20, 30]
#      ↑
# b ───┘

b.append(40)

print(a)
print(b)


# 3. Assignment

languages = ["Python", "Java"]
other_languages = languages

other_languages.append("C#")

# Both variables still use the same object
print(languages)
print(other_languages)


# 4. Copies

list_a = [1, 2, 3]
list_b = list_a.copy()

# Now they are different objects
#
# list_a -> [1, 2, 3]
# list_b -> [1, 2, 3]

list_b.append(4)

print(list_a)
print(list_b)


# 5. Sharing objects

def add_user(users):
    users.append("Carlos")


user_list = ["Ana", "Luis"]

add_user(user_list)

# The function receives a reference to the same list
print(user_list)