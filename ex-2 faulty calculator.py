num1=input("enter the first number")
operator=input("which operator do you want to use : ")
num2=input("enter the second number")
eq=num1+operator+num2

value1=555
value2=77
value3=4

str1="45*8"
str2="56+9"
str3="56/6"

num1 != num2 and num2 != num1

if eq==str1:
    print(value1)
elif eq==str2:
    print(value2)
elif eq==str3:
    print(value3)
else:
    eq=eval(num1+operator+num2)
    print(eq)
