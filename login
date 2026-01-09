#this is a login with just the user input.
#in this i have added restriction like "no spaces,numbers,and less than 12 characters".
username=input("enter your name:")
if len(username)>12:
    print("the username can not contain more than 12 characters!!")
elif not username.find(" ")== -1:
    print("the username can not contain spaces!!")
elif not username.isalpha():
    print("the username can not contain numbers!!")
else:
    print(f"hello {username}")
