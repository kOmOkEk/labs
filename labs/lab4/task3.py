date = input("Enter date in DD.MM.YYYY format: ")

def magical_date(date):
    if int(date[0:2]) * int(date[3:5]) == int(date[-2:]):
        return True
    else:
        return False

print(magical_date(date))

