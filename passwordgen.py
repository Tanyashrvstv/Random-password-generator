import random
import string 

total = string.ascii_letters + string.digits + string.punctuation

length = int(input("Enter length for password: "))

password = "".join(random.sample(total, length))

print(password)