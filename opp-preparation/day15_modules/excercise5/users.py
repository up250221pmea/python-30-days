

def create_full_name(first_name, last_name):
    return first_name + last_name


def create_user(name, age):
    datos = {'name': {name}, 'age':{age}}
    return datos

def is_adult(age):
    return age >= 18