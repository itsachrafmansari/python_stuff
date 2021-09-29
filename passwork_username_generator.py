import random
import string

while True:
    userLen = int(input("Username length : "))
    passLen = int(input("Password length : "))
    samples = int(input("Number of samples : "))
    for sample in range(samples):
        # Randomness generator
        un = string.ascii_letters + string.digits
        random_un = "".join(random.choice(string.ascii_letters) for i in range(userLen))
        pw = string.ascii_letters + string.hexdigits + string.punctuation
        random_pw = "".join(random.choice(pw) for x in range(passLen))

        # Print a random username and password
        print("\nUsername : {}  |  Password : {}".format(random_un, random_pw))
    input("\nPress ENTER to regenerate\n\n")  # Press ENTER to regenerate
