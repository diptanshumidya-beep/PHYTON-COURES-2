def  add(num1 , num2):
    return(num1 + num2)


def  subtract(num1 , num2):
    return(num1 - num2)



def  multiply(num1 , num2):
    return(num1 * num2)



def  divide(num1 , num2):
    return(num1 / num2)



num1 = int(input("Give a nummmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmber"))

num2 = int(input("Give a nummmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmber"))




print("a = Add" , "b = Subtract" , "c = multiply" , "d = divide")



opperater = input("Give an operator from below letters")




if opperater == "a" :
    print(add(num1 , num2))


if opperater == "b" :
    print(subtract(num1 , num2))


if opperater == "c" :
    print(multiply(num1 , num2))


if opperater == "d" :
    print(divide(num1 , num2))





