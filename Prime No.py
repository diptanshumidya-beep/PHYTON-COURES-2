num = int(input("Enter a number:"))

if num > 1:

    for i in range (2,int(num**0.5) + 1) :

        if num % i == 0:
            print("It is a not a prime number")

        else:
            print("It is a prime number")

else:
    print("It is not a prime number")

























