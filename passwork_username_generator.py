import random
import string

# You can change the username/password length from here :
username_length = 10
password_length = 20

while True:
    # Randomness generator
    un = string.ascii_letters + string.digits
    random_un = "".join(random.choice(un) for i in range(username_length))
    pw = string.ascii_letters + string.hexdigits + string.punctuation
    random_pw = "".join(random.choice(pw) for x in range(password_length))

    # Print a random username and password
    print("Username : ", random_un, " | ", "Password : ", random_pw)
    input('-' * 60)  # Press ENTER to regenerate
