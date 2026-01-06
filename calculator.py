operator = input("enter a operator( + - * / ):")
num1 = float(input("enter first number:"))
num2 = float(input("enter the second number:"))
if operator == "+":
  result = (num1+num2)
  print("the result is:",result)
elif operator == "-":
  result = (num1-num2)
  print("the result is:",result)
elif operator == "*":
  result = (num1*num2)
  print("the result is:",result)
elif operator == "/":
  result = (num1/num2)
  print("the result is:",result)
else:
  result = "invalid operator"
print(result)
