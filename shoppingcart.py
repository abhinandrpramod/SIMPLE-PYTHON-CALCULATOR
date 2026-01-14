items=[]
prices=[]
total=0
while True:
    item=input("enter the item (enter e for exiting):")
    if item.lower()=="e":
        break
    else:
        price=float(input(f"enter the price of {item}:$"))
        items.append(item)
        prices.append(price)
print("------YOUR CART------")
for item in items:
    print(item,end=" ")
for price in prices:
    total+=price

print()
print(f"your cart value is:${total}")
