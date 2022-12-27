import random
upper_case = 'QWERTYUIOPASDFGHJKLMNBVCXZ'
lower_case = 'qwertyuiopasdfghjklmnbvcxz'
symbol = '*(){}[]@<>?+!#$_-'
number = '0123456789'
length = int(input('how many characters do you want your password to be? '))
while True:
    if length < 8:
        print('password must be between 8 to 16 characters')
        length = int(input('how many characters do you want your password to be? '))
    elif length > 16:
        print('password must be between 8 to 16 characters')
        length = int(input('how many characters do you want your password to be? '))
    else:
        password = upper_case + lower_case + symbol + number
        final = ''.join(random.sample(password, length))
        print(f'you new password is👉👉 {final}')
        break
