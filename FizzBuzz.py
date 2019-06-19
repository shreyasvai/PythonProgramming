# Prints numbers from 1 to 100. If divisble by 3, prints
# "Fizz". If divisble by 5, prints "Buzz", and if divisible
# by 3 an 5, prints "FizzBuzz" all instead of the numbers

a = 1  # will be used as the counter to go from 1-100

while a <= 100: # iterates through 100 terms
    if a % 3 == 0 and a % 5 == 0: # checks to see if divisble by both 5 and 3 first
        print("FizzBuzz")
    elif a % 3 == 0: # else checks if divisble by 3
        print("Fizz")
    elif a % 5 == 0: # else checks if divisible by 5
        print("Buzz")
    else: # if not divisible by either, prints the number
        print(a)
    a = a + 1