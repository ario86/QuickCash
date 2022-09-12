# main


# global var stored
wallet = 0
email = "ario26@"
password = "1234"
p_b = 0


def add_money(a):
    global wallet
    # axis to use global var as local var inside the func

    wallet += a
    print("Updated wallet amount: ", wallet)


def view_wallet():
    print("the wallet amount: ", wallet)


def user_reg(self, email, password):
    
    self.email=email
    self.password=password
    self.admin_details={'email': self.email, 'Password':self.password}
    print('\n!Registration Successful!\n')
   
    

def user_login(self, email, password):
    if len(self.user_details)!=0:
        if email== self.admin_details['email'] and password==self.admin_details['Password']:
            print('\n!Successful Login !')
            
        else:
            print('\nInvalid Credentials\n')
    else:
        print('\nInvalid Credentials\n')

def mobile_recharge():
    global p_b
    char='a'
    b = int(input("select recharge plan    149,251,399,499,681: "))
    p_b += b
    mob_num=input("Enter 10 digit mobile no: ")

    l = [149, 251, 399, 499, 681]
    if (b in l) and (len(mob_num)==10) and (char not in mob_num):
        print("updated pack_bal: ", p_b)
    else:
        print("invalid amount or number")


def view_pack_bal():
    print("your current pack_bal: ", p_b)


# driver

while True:
    print("\n\n!!Welcome to QuickCash!!\n\n0. mobile recharge\n1. add money\n2. user registration\n3. user login\n4. view wallet bal\n5. view pack balance\n6. exit\n\nchoose an optiion to continue: ")

    choose = int(input())

    if choose == 0:
        mobile_recharge()
        print("press x to quit")
        if choose == "x":
            print("thankyou for using QuickCash")
        print("\npress c to continue\n")




    elif choose == 1:
        x = int(input("enter the amount: "))
        add_money(x)
        print("press x to quit")
        if choose == "x":
            print("\nthankyou for using QuickCash")
        print("\npress c to continue\n")

    elif choose == 2:
        user_reg(email, password)
        print("press x to quit")
        if choose == "x":
            print("\nthankyou for using QuickCash\n")
        print("\npress c to continue\n")


    elif choose == 3:
        email = input("enter email: ")
        password = input("enter password: ")
        user_login(email, password)
        print("\npress x to quit or c to continue\n")

        if choose == "c":
            print("press c to continue")
        elif choose == "x":
            print("\nthankyou for using QuickCash\n")
            break


    elif choose == 4:
        view_wallet()
        print("\npress c to continue")

    elif choose == 5:
        view_pack_bal()
        print("\npress c to continue")

    elif choose == 6:
        print("\nthankyou for using QuickCash\n")
        break


    else:
        print("\ninvalid option")

    choose2 = input()

    if choose2 == "c":
        continue

    elif choose2 == "x":
        print("thankyou for using QuickCash\n")
        break

    else:
        print("\nInvalid option")
