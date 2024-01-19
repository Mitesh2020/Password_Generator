import string
import random

s1 = string.ascii_lowercase #abcdefghijklmnopqrstuvwxyz
s2 = string.ascii_uppercase #ABCDEFGHIJKLMNOPQRSTUVWXYZ
s3 = string.digits #0123456789
s4 = string.punctuation #!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~


print()
pass_len = int(input("Enter password length : "))
s = []
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
password = random.shuffle(s)
print()
print("Generated Password : "+"".join(s[0:pass_len]))
print()