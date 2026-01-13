temp=float(input("Enter the temperature:"))
unit=input("Is the temperature in celsius or fahrenheit (C/F):")
if unit.upper() == "F":
    temp=((temp-32)*5/9)
    print(f"{round(temp,1)}C")
elif unit.upper() == "C":
    temp=((temp*(9/5))+32)
    print(f"{round(temp,1)}F")
else:
    print(f"{unit} is not valid")
