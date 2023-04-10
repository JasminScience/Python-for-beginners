# Rock, paper, scissors 
# 'Solution'
from random import randint
game = ['x', 'p', 's']
user = input('<')
pc = game[(randint(0,2))]
if user == 'x' and pc == 'p':
    print('pc wins')
elif user == 'x' and pc == 's':
    print('user wins')
elif user == 'p' and pc == 's':
    print('pc wins')
elif user == 'p' and pc == 'x':
    print('user wins')
elif user == 's' and pc == 'x':
    print('pc wins')
elif user == 's'  and pc == 'p':
    print('user wins')                   
