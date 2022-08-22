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


def user_reg(new_email, new_password):
    new_email = input("enter email: ")
    new_password = input("enter password: ")
    print("!successfully registered!")


def user_login(e, p):
    global email
    global password

    if (e == email) and (p == password):
        print("!log in successful!")
    else:
        print("Invalid credentials.")


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
        print("press c to continue")




    elif choose == 1:
        x = int(input("enter the amount: "))
        add_money(x)
        print("press x to quit")
        if choose == "x":
            print("thankyou for using QuickCash")
        print("press c to continue")

    elif choose == 2:
        user_reg()
        print("press x to quit")
        if choose == "x":
            print("thankyou for using QuickCash")
        print("press c to continue")


    elif choose == 3:
        email1 = input("enter email: ")
        password1 = input("enter password: ")
        user_login(email1, password1)
        print("press x to quit or c to continue")

        if choose == "c":
            print("press c to continue")
        elif choose == "x":
            print("thankyou for using QuickCash")
            break


    elif choose == 4:
        view_wallet()
        print("press c to continue")

    elif choose == 5:
        view_pack_bal()
        print("press c to continue")

    elif choose == 6:
        print("thankyou for using QuickCash")
        break


    else:
        print("invalid option")

    choose2 = input()

    if choose2 == "c":
        continue

    elif choose2 == "x":
        print("thankyou for using QuickCash")
        break

    else:
        print("Invalid option")
