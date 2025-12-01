import random
import string

def password(length: int):
    password = ""
    for i in range(length):
        password+=random.choice(string.ascii_letters+string.digits+string.punctuation)
    return password

print(password(int(input("how long do you want the password? "))))