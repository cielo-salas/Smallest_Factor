def smallest_factor(n):
    for i in range(2, n + 1):  # i is the factor of n(input)
        if n % i == 0:
            return i  # it will return i if the remainder is 0


# Usage of the defined operation above
number = int(input("Enter an integer number >= 2:"))
result = smallest_factor(number)

print(f"The smallest factor of {number} other than 1 is {result}.")

while True:
    if number < 2:
        print("Invalid input enter a number greater than 2.")
        break