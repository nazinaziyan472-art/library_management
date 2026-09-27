import json
class user:
    def __init__(self):
        self.username=""
        self.password=""
    def signup(self):
        self.username=input("enter the username: ")
        password= input("enter the password: ")
        confirm_password=input("confirm password: ")
        if password==confirm_password:
            self.password=password
            user_data={"username":self.username,"password":self.password}
            with open("user.json","r")as file:
                users=json.load(file)
                users.append(user_data)
            with open("user.json","w")as file:
                json.dump(users,file,indent=4)
            print("signup successfully")
        else:
            print("password does not match")

    def login(self):
        username=input("enter the username: ")
        password=input("enter the password: ")
        with open("user.json","r")as file:
            users=json.load(file)
            for user in users:
                if user["username"]==username and user["password"]==password:
                    print("login successfully")
                    return
                print("invalid username or password")

    def logout(self):
        print("logout successfully")