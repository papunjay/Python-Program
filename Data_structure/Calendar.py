def isLeapyear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
year=int(input())
month=int(input())

months=["January", "February", "March",
            "April", "May", "June",
            "July", "August", "September",
            "October", "November", "December"]
days=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]