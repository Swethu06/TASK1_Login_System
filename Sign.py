counter=0
c=0
#For registration of new user
def register():
    global m
    global User_name
    with open("login.txt", "r") as db:
    #db = open("login.txt", "r")
        User_name = input("Create username :")
        m = user_id_validation(User_name)
        send_password()
#Password creation
def send_password():
    global c
    if m==True:
        Password = input("Create password :")                                                                           #If both password and confirm possword not matches for 3 times,
        n = password_validation(Password)                                                                               #Displays account lock message
        while c<3:
            if n==True:
               Password1 = input("confirm password :")
               s = []
               p = []
               with open("login.txt", "r") as db:
                #db = open("login.txt", "r")
                for i in db:
                    a, b = i.split(", ")
                    b = b.strip()
                    s.append(a)
                    p.append(b)
                data = dict(zip(s, p))
                if Password != Password1:
                    print("Password do not match with the confirm password.Please re-register")
                    c += 1
                else:
                    if len(Password) <= 6:
                        print("Password is too short,re-register")
                        c += 1
                    elif User_name in s:
                        if option1=='1':                                                                                #User name exists< then he has to enter new user name
                            print("User name already exists. Please create a new user name")
                            c += 1
                            register()
                            break
                        else:
                            if option1=='3':
                                if option2=='1':
                                   with open("login.txt", "w") as db:                                                   #This step is for creating new password,
                                    #db = open("login.txt", "w")                                                        #if the user has forgotten the password.
                                    up_dict = {User_name: Password}                                                     #The new password will be updated in the old password.
                                    data.update(up_dict)                                                                #w - mode file is used, since overrides the entire content
                                    for key, val in data.items():                                                       #and updates the new password along with the old username
                                        db.write(key + ", " + val + "\n")
                                    print("Password successfully created")
                                    print("Hi, Welcome to Guvi ")
                                    break
                    else:
                        #db = open("login.txt", "a")
                       with open("login.txt", "a") as db:                                                               #No username exists, then the username and password are updated.
                        db.write(User_name + ", " + Password + "\n")
                        print("Username successfully registered")
                        print("Hi, Welcome to Guvi ")
                        break
        else:
            print("Your account has been locked since you have tried two many times.Please try after sometime")
#Login validation
def user_id_validation(x):
    import re
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if (re.fullmatch(regex, x)):
        return True
    else:
        print("Enter the valid Email :")
        if option1=='1':register()
        elif option1=='2':access()
        else:forgot_password()
#Login process
def access():
   with open("login.txt", "r") as db:
    #db = open("login.txt", "r")
    global User_name
    User_name = input("Enter your username :")
    m = user_id_validation(User_name)
    if m==True:
      Password = input("Enter your password :")
      m2=password_validation(Password)
      if m2==True:
          s = []
          p = []
          for i in db:
            a, b = i.split(", ")
            b = b.strip()
            s.append(a)
            p.append(b)
          data = dict(zip(s, p))
          try:
            if data[User_name]:
                try:
                    if Password == data[User_name]:                                                                     #If username and password matches with the file, then the user can login
                        print("Successfully Logged in")
                        print("Hi, Welcome to Guvi ")
                    else:
                        Print("Password is incorrect")
                except:
                    print("Incorrect password of username")                                                             #If we gives the wrong password then he can access forgot password for login in
                    forgot_password()
            else:
                print("Username or Password does not exists")
          except:

            print("Username does not exists.Please go for registration")                                                #If no user name exists, then the user name has an option to register
            register()
    else:
        print("Login again with the user name and Please provide the correct password")
        access()

#Forgot password - User has can either choose to create a new password or retrieve the existing password
def forgot_password():
   global User_name
   global m
   global option2
   with open("login.txt", "r") as db:                                                                                   #with is used so that at the end of file,it will be automatically closed
    #db = open("login.txt", "r")
    User_name = input("Enter the Username: ")
    m = user_id_validation(User_name)
    if m==True:
            print(" 1 - Create New password | 2 - Retrieve")
            option2 = input("Enter your choice:")
            if option2 == '1':
                send_password()
            elif option2 == '2':
                s = []
                p = []
                for i in db:
                    a, b = i.split(", ")
                    b = b.strip()
                    s.append(a)
                    p.append(b)
                data = dict(zip(s, p))
                with open("login.txt", "r") as db:                                                                      #Read file to get the password for the given user name
                #db = open("login.txt", "a")
                 rev_password = data.get(User_name)
                 print("Your Password is", {rev_password})
                 print("Please login in with the retrieved password")
                 access()
            else:
                opt()
    else:
        opt()
#Password validation using re expression
def password_validation(x):
    import re
    check_length = len(x)
    if check_length < 16 and check_length > 5:                                                                          #Checks for length
        global counter
        while counter < 3:
            if re.findall("^.*(?=.{8,16})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$",x):
            #if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,16}', x):                                                          #Another method for validation
                return True
        else:                                                                                                           #Counter is set to 3(within the loop) because user has option
                counter = counter + 1                                                                                   #of resetting the password thrice
                print("""Password must meet the following requirements :                                                
                                    Password length should be in between 5 and 16
                                    At least minimum one Special character
                                    At least one Upper case
                                    At least one Digit
                                    At least one Lower case""")
                print("Re-enter the valid Password ")
                if counter == 3:
                    print("Your account has been locked since you have tried two many times.Please try after sometime")
                    break
                if option1 == '1':
                    send_password()
                    break
                else:
                    if option1 == '2':
                        access()
                        break
    else:
        print("Password length should be in between 5 and 16")
        if option1 == '1':
            send_password()
        else:
            if option1 == '2':
                access()
#Options for login by user
def opt(option=None):
    global option1
    print("Welcome to GUVI Data science Course")
    print("*"*35)
    print("1-Register | 2-Login | 3-Forgot Password")
    option = input("Enter your choice:")
    if (option) == '2':
        option1 = option
        access()
    elif option == '1':
        option1 = option
        register()
    elif option == '3':
        option1 = option
        forgot_password()
    else:
        print("Enter the valid option")
        opt()
opt()










#Another method of password validation
# def password_validation(x):
#     p = []
#     l = u = s = n = 0
#     check_length = len(x)
#     if check_length < 16 or check_length > 5:
#         for i in x:
#             if i.isdigit():
#                 n = n + 1
#             elif i.isupper():
#                 u = u + 1
#             elif i.islower():
#                 l = l + 1
#             else:
#                 if i in '!@#$%^&*_-':
#                     s = s + 1
#     global counter
#     while counter < 3:
#         if (u >= 1 and l >= 1 and s >= 1 and n >= 1) and (u + l + s + n) == len(x):
#             return True
#         else:
#             counter = counter + 1
#             print("""Password must meet the following requirements :
#                                     Password length should be in between 5 and 16
#                                     At least minimum one Special character
#                                     At least one Upper case
#                                     At least one Digit
#                                     At least one Lower case""")
#             print("Re-enter the valid Password ")
#             if counter == 3:
#                 print("Your account has been locked since you have tried two many times.Please try after sometime")
#                 break
#             if option1 == '1':
#                 send_password()
#             else:
#                 if option1 == '2':
#                     access()