user_input = input("enter (register)/(login): ")
# stage 1 registration
def getdetails():
    import re
    regex = r'\b[A-Za-z]+[A-Za-z0-9._%+-]+@[A-Za-z]+\.[A-Z|a-z]{2,}\b'
    while True:
        user_name = input("enter your emailid or username: ")
        email = False
        if re.fullmatch(regex, user_name):
            email = True
            break
        else:
            print("invalid")
    if True:
        print("valid")
    
    import re 
    while True:
        password = input("Enter your password : ") 
        pswrd = False 
        if (len(password)<6 or len(password)>16): 
            print("Not valid ! Total characters should be between 6 and 16") 
            continue 
        elif not re.search("[A-Z]",password):
            print("Not valid ! It should contain one letter between [A-Z]")
            continue 
        elif not re.search("[a-z]",password):
            print("Not valid ! It should contain one letter between [a-z]") 
            continue
        elif not re.search("[1-9]",password): 
            print("Not valid ! It should contain one letter between [1-9]") 
            continue 
        elif not re.search("[~!@#$%^&*]",password): 
            print("Not valid ! It should contain at least one letter in [~!@#$%^&*]") 
            continue 
        elif re.search("[\s]",password): 
            print("Not valid ! It should not contain any space") 
            continue
        else:
            pswrd = True
            break
    if(True):
        print("Password is valid")

    # stage 2
    with open(f"{user_name}", "w") as f:
        f.write(f"{password}")

def checkdetails():
    user_input = input("enter (register)/(forgot password): ")
    if user_input == "forgot password":
        user_name = input("enter your emailid or username: ")
        try:
            with open(f"{user_name}") as f:
                b = f.read()
                print(b)
        except FileNotFoundError:
            print("register")
            getdetails()
    if user_input == "register":
        getdetails()

if user_input == "register":
    getdetails()
# stage 3 login
if user_input == "login":
    user_name = input("enter your emailid or username: ")
    password = input("enter password: ")
    try:
        with open(f"{user_name}") as f:
            a = f.read()
        if a == password:
            print("valid")
        else:
            print("invalid")
            checkdetails()
    except FileNotFoundError:
        print("not valid")
        checkdetails()
