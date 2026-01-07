temp=float(input("Enter the temperature:"))
unit=input("Is the temperature in celsius or fahrenheit (C/F):")
if unit == "F":
    temp=((temp-32)*5/9)
    print(round(temp,1))
elif unit == "C":
    temp=((temp*(9/5))+32)
    print(round(temp,1))
else:
    print(f"{unit} is not valid")