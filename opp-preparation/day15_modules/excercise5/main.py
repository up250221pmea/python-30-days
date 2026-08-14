# Exercise 5 

from users import create_full_name, create_user, is_adult


first_name = "John"
last_name = "Smith"
age = 20

full_name = create_full_name(first_name, last_name)

user = create_user('John', age)

adult = is_adult(age)

print(f"Full name: {full_name}")
print(f"User: {user}")
print(f"Is adult: {adult}")