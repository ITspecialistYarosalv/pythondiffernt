import random
import string
sequence = input("Your password eskiz - ")

length = int(input("What is the length of your password - "))

baselist = [*sequence]

random.shuffle(baselist)
password = []
for i in range(length):
    bch = random.choice(baselist)
    stc = random.choice(string.ascii_lowercase)
    dc = random.choice(string.digits)
    sc = random.choice(string.punctuation)
    password.append(random.choice([bch,stc,dc,sc]))

pas = ''.join(password)

print(pas)
