""" Design a simple calculator with basic arithmetic operations.
    Prompt the user to input two numbers and an operation choice.
     Perform the calculation and display the result."""

num1=int(input("Enter first number:"))
num2=int(input("Enter Second number:"))

choice=int(input("Enter your choice:"))

#Enter your choice.
if choice==1:   

    # addtion of two number;
    num=num1+num2
    print("Addition:",num)

elif choice==2:
    #Subtraction of two number 
    num=num1-num2
    print("Subtraction:",num)

elif choice==3:
    # Multiplication of two number:
    num=num1*num2
    print("Multiplication:",num)

elif choice==4:
    # Division of two number:
    num=num1/num2
    print("Division:",num)

else:
    print("Invalid your choice:")
