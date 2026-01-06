operator = input("enter a operator( + - * / ):")
num1 = float(input("enter first number:"))
num2 = float(input("enter the second number:"))
if operator == "+":
  result = (num1+num2)
elif operator == "-":
  result = (num1-num2)
elif operator == "*":
  result = (num1*num2)
elif operator == "/":
  result = (num1/num2)
else:
  result = "invalid operator"
print("the result is:",result)
