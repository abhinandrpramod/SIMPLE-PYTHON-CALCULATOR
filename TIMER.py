import time
mytime=int(input("Enter the time to wake up in seconds:"))
for x in range(mytime,0,-1):
    seconds=x%60
    minutes=int(x/60)%60
    hour=int(x/3600)
    print(f"{hour:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("TIME TO WAKE UP!!!")
