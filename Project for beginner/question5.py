# Password Generator Python Project
# 'Solution'
import random
print('Here are passwords :) ')
char = 'abcdefghijklmnopqrstshthvxxhuwz1234567890!@#$%^&*()<>?,.;'
number = int(input('Please give me amount of passwords '))
length = int(input('Chose the len of passwords'))
for x in range(number):
    passwords = ''
    for y in range(length):
        passwords += random.choice(char)
    print(passwords)    















