def leapYear(year):
    if(year % 4) == 0:
         if(year % 400) == 0:
            print("{0} is a leap year: ".format(year))
        else:
            print("{0} is not leap year: ".format(year))


if __name__ == '__main__':
    print(leapYear(2000))