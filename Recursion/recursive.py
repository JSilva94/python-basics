def factorial(n):
    if n == 0:
        return 1
    else:
        print(n)
        return n * factorial(n-1)

factorial(4)

def rec_sum(n):
    if n < 1:
        return 0
    else:
        return n + rec_sum(n-1)

rec_sum(5)

def sum_func(n):
    if n < 10:
        return n
    else:
        
        return n % 10 + sum_func(n//10)

sum_func(5)
sum_func(5442323478)

def reverse(s):
    if(len(s) == 1):
        return s
    else:
        return s[-1] + reverse(s[:len(s)-1])
 
reverse("hello world")

def permute(s):
    if len(s) == 1:
        return 1
    else:
        return len(s) * permute(s[1:])

permute('abc')


def fib(n):
    if n<4:
        return 1
    else:
        return fib(n-1) + fib (n-2)

fib(4)

value = 0

def fib2(n):
    global value
    if n < 4:
        value +=1
    else:
        value += fib(n-1) + fib(n-2)

fib(4)

def fib3(n):
    two_back = 0
    one_back = 1
    value = 0
    for i in range(n):
        value += two_back + one_back
        two_back = one_back
        one_back = i
    return value

fib(7)

num_of_coins = 1

def rec_coins(target,coins):
    min_coins = target
    smallest = coins[0]
    if target in coins:
         return 1

    else:
        for c in coins[1:]:
            if c < smallest:
                smallest = c



    
    return min_coins
    

