ticket = input("Enter ticket number: ")
length = len(ticket)
if length % 2 == 0:
    cut = length // 2
    if sum(map(int, ticket[:cut])) == sum(map(int, ticket[cut:])):
        print("Lucky number")
    else:
        print("Not lucky number")
else:
    print("Invalid ticket")

