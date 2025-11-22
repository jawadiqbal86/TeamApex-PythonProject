print("\t*** Welcome to Calculator App ***")
num1=float(input("Enter First Number: "))
num2=float(input("Enter Second Number:"))
while True:
    print("\nSelect Operation")
    oper=int(input("1) Addition\n2) Subtraction\n3) Multiplication\n4) Division\n"))
    print()
    if(oper==1):
        print(num1, "+" ,num2, "=" ,num1+num2)
    elif(oper==2):
        print(num1, "-" ,num2, "=" ,num1-num2)
    elif(oper==3):
        print(num1, "*" ,num2, "=" ,num1*num2)
    elif(oper==4):
        print(num1, "/" ,num2, "=" ,num1/num2)
    else:
        print("\nInvalid Selection Try again")
    again=int(input("\nInput 1 to perform operation on same numbers\nInput 0 to exit the App\n"))
    if(again==0):
        break
print("\nThank you for using this App, Good bye")