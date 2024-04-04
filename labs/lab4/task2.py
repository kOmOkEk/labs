def divide_100_on_smth(num):
    if 100 % num == 0:
        return f"100 is divisible by {num}, this is the result of division: {100 // num}"
    else:
        return f"100 isn't divisible by {num}, but this is the result of division: {100 / num}"

try:
    b = int(input("Enter a number: "))
    print(divide_100_on_smth(b))
except ZeroDivisionError:
    print("Can't divide by zero")
except ValueError:
    print("please enter a number, not a word")

