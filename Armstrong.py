num  = (input("Give a number "))

j = 0

for i in num:
   j =   int (i) ** 3 + j



print(j)

if j == int(num):
   print("It is a armstrong number")


else:
   print("It is not an armstrong number")