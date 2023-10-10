print("***************************CALCULATOR*************************")

print("\n 1. Addition")
print("\n 2. Subtraction")
print("\n 3. Multiplication")
print("\n 4. Division")

val = int(input("\n Enter any given value to perform that specified operation:"))

if val in [1, 2 ,3, 4]:
    n1 = int(input("\n Enter the first number:"))
    n2 = int(input("\n Enter the second number:"))
    if val==1:
        print(n1, "+", n2, "=", n1+n2)
    elif val==2:
        print(n1, "-", n2, "=", n1-n2)
    elif val==3:
        print(n1, "*", n2, "=", n1*n2)
    else:
        print(n1, "/", n2, "=", n1/n2)
else:
    print("\n Invalid Input")
