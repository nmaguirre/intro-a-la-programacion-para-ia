def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Fuzz'
    else:
        return n

x = 1
while x <= 100:
    print(fizzbuzz(x))
    x = x + 1


