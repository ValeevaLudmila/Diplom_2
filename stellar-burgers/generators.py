from faker import Faker

fake = Faker()

def email_generator():
    return fake.email()

def password_generator():
    return fake.password(length=10)

def name_generator():
    return fake.first_name()