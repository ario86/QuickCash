# main code

def wallet():
    print("!! Your wallet !!")
    wallet=0
    a=int(input("enter amount : "))
    wallet= wallet+a # 0+10=10, 10+100=110
    print("updated wallet amount: ", wallet)


def user_reg(): 
    print("!!user reg !!")
    name=input('name : ')
    age=input("age : ") 
    
def email(): 
    email=input("email : ")
    print("succesfully registered")
    
def admin_reg():
    print("!! admin_reg !!")
    email=input("email_id : ")

def password():
    password=input(" password: ")
    print("succesfully registered")
    
    

def mobile_recharge():
    
    pack_bal=0
    b=int(input("amount : "))
    pack_bal= pack_bal+b
    print("updated pack balance: ", pack_bal)    

    
    
def admin_login():
    print("!! Admin login !!")
    new_email=input()
    new_password=input()
    
    
    
def user_login():
    print("!! User login !!")
    new_email=input()
    new_password=input() 
    
    
    if new_email == email and new_password == password:
            print("login succesful")       
    else:
        print("Invalid credentials ⚠ Repeated failed attempts will block your bank account for 48h. Try again later")
        




# driver code  
      

if __name__=="__main__":
    print("welcome to QuickCash") 
    while True:

        print("0. mobile_recharge\n1. add money\n2. user_reg\n3. admin_reg\n4. user_login\n5. admin_login\n6. exit")

        x= input("enter any above no : ")


        
        if x=="0":
            mobile_recharge()
        
        elif x=="1":
            wallet()

        elif x=="2":
            user_reg()

        elif x=="3":
            admin_reg()

        elif x=="4":
            user_login()
            
        elif x=="5":
            admin_login()
            
        elif x=="6":
            print("Thank you for using QuickCash ☺")
            break
        
        else:
            print("Please enter corrct number" )
            
            
    
            

        
