import time


n = 5
words = ["five", 'four', 'three', 'two', 'one']
time.sleep(1)
print('''
This is NASA ultimate rocket launch sequence, 
our major rocket is about to launch into space.
Are you ready to witness the greatest thing in your life?
Yes or No
''')
time.sleep(2)
loop = input('Yes or No: ').lower()
chances = 3
while True:
    if loop == 'yes':
        time.sleep(0.5)
        print('ok then welcome aboard blast off starts in')
        time.sleep(0.7)
        while n > 0:
            for word in words:
                print(f'{n}- {word}')
                n -= 1
                time.sleep(1.2)
        print("BLASTOFF, YAAY")
        break
    elif loop == 'no':
        print("aww snap you ain't man enough hope to see you in our next blastoff ceremony")
        break
    elif chances == 0:
        print('''
you are not ready.
Abeg getat
                ''')
        break
    else:
        print('answer must be yes or no')
        print('behave yourself')
        time.sleep(0.5)
        loop = input('Yes or No: ').lower()
        chances -= 1
values = '''input("input the names you want: ")
lone = values.split(", ")
shift = ""
finale = []
while len(lone) > 0:
    shift = random.choice(lone)
    lone.remove(shift)
    finale.append(shift)
print(finale)'''
