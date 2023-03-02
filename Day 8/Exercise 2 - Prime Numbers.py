#Write your code below this line 👇
def prime_checker(number):
    i = 2
    limit = 0

    if number == 0 and number == 1:
        limit = 1

    while i <= number / 2:
        if number % i == 0:
            limit += 1
        i += 1
    
    if limit == 0:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)