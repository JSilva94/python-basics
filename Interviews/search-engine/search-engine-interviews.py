import random

def roll7():
    return random.randint(1,7)

def roll5():
    return random.randint(1,5)


def five_sided_dice():
    roll = 6

    while roll > 5:
        roll = roll7()
        print('you rolled a ' + str(roll))
    return roll


def seven_sided_dice():
    roll1 = roll5()
    roll2 = roll5()

    while roll1 + roll2 > 7:
        roll1 = roll5()
        roll2 = roll5()
    return roll1 + roll2



def recursive_recursion(str):
    if len(str) == 1:
        return str
    return str[-1] + recursive_recursion(str[0:-1])

for i in range(2):
    print(i)
print(recursive_recursion('hello jkdsbds'))

def sqr_root(n):
    i = 1
    while i*i <= n:
        i+=1
    
    return i-1

print(sqr_root(24))
print(five_sided_dice())
print(seven_sided_dice())
