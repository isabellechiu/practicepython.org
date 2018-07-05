#Exercise 16
#Password Generator
#Write a password generator in Python.
#Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
#The passwords should be random, generating a new password every time the user asks for a new password.
#Include your run-time code in a main method.
#Extra:
#Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

#My first answer without using function
import random
num = random.sample(range(0, 9), 5)
import string
u_case = random.sample((string.ascii_uppercase), 5)
l_case = random.sample((string.ascii_lowercase), 5)
p = random.sample((string.punctuation), 5)
pwd = [num, u_case, l_case, p]
print(pwd)
#Need to convert the list to string. Otherwise, AttributeError: 'list' object has no attribute 'split'.

#list1 = ['1', '2', '3']
#str1 = ''.join(list1)
#print(str1)

num = ''.join(str(e) for e in num)
u_case = ''.join(u_case)
l_case = ''.join(l_case)
p = ''.join(p)
pwd = [num, u_case, l_case, p]
print(pwd)
pwd = ''.join(str(f) for f in pwd)
print(pwd)

#Using the function
def generate(pwd):
    import random
    num = random.sample (range (0, 9), 5)
    import string
    u_case = random.sample ((string.ascii_uppercase), 5)
    l_case = random.sample ((string.ascii_lowercase), 5)
    p = random.sample ((string.punctuation), 5)
    pwd = [num, u_case, l_case, p]
    num = ''.join(str(e) for e in num)
    u_case = ''.join(u_case)
    l_case = ''.join(l_case)
    p = ''.join (p)
    pwd = [num, u_case, l_case, p]
    pwd = ''.join(str(f) for f in pwd)
    return print(pwd)

generate(pwd)

#The answer
# generate a password with length "passlen" with no duplicate characters in the password
# By using (''.join )to convert the list to string
import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = 8
p = random.sample(s,passlen)
print(p)

p = ''.join(random.sample(s,passlen))
print(p)

#The best other answer
import string
import random

def pw_gen(size = 20, chars=string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for a in range(size))

print(pw_gen(int(input('How many characters in your password?'))))


#The other cool answer

import random

characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
              'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
              'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5',
              '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '&', '*', '(', ')']

strength = input("Do you want a weak, medium, or strong, password?: ").lower()

new_password = []

def password(strength):
    if strength == 'weak':#First we'll define the strength
        while len(new_password) != 5:
            new_password.append(characters[random.randint(1, 70)])
    elif strength == 'medium':
         while len(new_password) != 8:
             new_password.append(characters[random.randint(1, 70)])
    elif strength == 'strong':
        while len(new_password) != 14:
            new_password.append(characters[random.randint(1, 70)])
            return new_password

password(strength)

new_password = "".join(new_password)

print(new_password)