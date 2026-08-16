from math import sqrt
number = int(input("Enter your number : "))
if number > 1:
    for i in range(2,(int(sqrt(number)))+1):
        if (number % i ) == 0:
            print("Its not a prime number. ")
            break
    else:
        print("Its a prime number . ")
else:
    print("Not a prime number / valid number")