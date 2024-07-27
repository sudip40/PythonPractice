# Write your code below this line 👇
def prime_checker(number):
    sqrt_number = int(number ** 0.5)
    checker = False
    for num in range(2, sqrt_number + 1):
        if number % num == 0:
            checker = True
            break

    if checker:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input())  # Check this number
prime_checker(number=n)