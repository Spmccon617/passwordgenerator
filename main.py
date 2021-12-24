import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "123456789"
special = "(){}[]_;|!?@"

all = lower + upper + number + special
length = 9
password = "".join(random.sample(all, length))

print("The password you generated is: ", password)
