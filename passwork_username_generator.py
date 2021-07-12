import random
import string

# You can change the username/password length from here :
username_length = 10
password_length = 20

while True:
    for t in range(8):
        # Randomness generator
        un = string.ascii_letters + string.digits
        random_un = "".join(random.choice(string.ascii_letters) for i in range(10))
        pw = string.ascii_letters + string.hexdigits + string.punctuation
        random_pw = "".join(random.choice(pw) for x in range(password_length))

        # Print a random username and password
        print("Username : {}  |  Password : {}\n{}".format(random_un, random_pw, "-" * 60))
    input()  # Press ENTER to regenerate
