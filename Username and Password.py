userpass={"hi":"12","bye":"34","see":"56","you":"78","me":"90"}
username=input("Enter your username:")
if username in userpass:
    password=input("Enter your password:")
else:
    print("You are not a valid user")
if password==userpass[username]:
    print("Login succesfull!")
else:
    print("Wrong password!")