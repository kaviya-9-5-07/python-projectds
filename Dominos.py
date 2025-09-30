import random
class Dominos:
    menu={"veg":{"margerita":129,"cheese_and-corn":169,"peppi_panner":260,"veg_loaded":210,"tomato_tangi":170},
          "non_veg":{'pepper barbique':199,'non_veg_loaded':169,'chicken_sausage':200},
          "snacks":{'garlic_bread':120,"french fries":95,'zingy':59,'chicken_cheese_balls':170},
          "desserts":{'choco_lava':150,'mousse_cake':170},
          "drinks":{'coke':90,'pepsi':78,'sprite':50}
    }
    def __init__(self,name,email,phno):
        self.name=name
        self.email=email
        self.phno=phno
        self.login_status=False  #to validate login state
        self.cart={}  #to store orders 

        #main program.
        while True:
              if not self.login_status:     
                print("-------------WELCOME TO DOMINOS🍕🍕 APP--------------")
                print("Login")
                ch=input("Do you want to login? (y/n):").lower()
                if ch=='y':
                    self.login()
              if self.login_status:
                    print("User👸🏻:" , self.name)
                    print("Enter 1: order🍲")
                    print("Enter2: show cart💸")
                    print("Enter 3: Logout➡️")
                    choice=int(input("Enter choice: "))
                    if choice==1:
                        self.order()
                    elif choice==2:
                        self.show_cart()
                    elif choice==3:
                        self.Logout()
                    else:
                        print("Invalid choice")
    @staticmethod
    def validate_otp(value):
        while True:                
                print("----------------------------")
                og_otp=random.randint(1000,9999)
                print(f"An otp has been sent to {value}")
                print(f"Your dominos otp is: {og_otp}")
                otp=int(input("Enter otp:"))
                if otp==og_otp:
                    print("Login successfully✅")
                    return True
                print("incorrect otp enter correct otp...")
    def login(self):
        print("Enter 1: login with phno")
        print("Enter 2: login with email")  
        ch=int(input("Enter chocie:"))
        if ch==1:
            phno=int(input("Enter phno:"))
            if phno==self.phno:
                state=self.validate_otp(phno)
                self.login_status=state
                         
            else:
                print("Incorrect phno")
        elif ch==2:
            email=input("enter email:")
            if email==self.email:
                state=self.validate_otp(email)
                self.login_status=state 
            else:
                print("Incorrect email")
        else:
            print("Invalid choice")
    def order(self):
        print("------🫚 dominos menu 🫚---------")
        for category in Dominos.menu:
            print(category)
        cat=input("Enter category: ")
        if cat in Dominos.menu:
            d=Dominos.menu[cat]
            for item in d:    #display items of respective category
                print(item,'        Rs.',d[item]) 
            item=input("Enter item: ")
            if item in d:
                q=int(input("Enter  quantity: "))
                if item in self.cart :
                    self.cart[item]+=d[item]*q
                else:
                    self.cart[item]=d[item]*q
                    print(f"{item} added to the cart🛒")  
                    print(self.cart)
            else:
                print(f'{item} is not available❌')
            
        else:
            print(f'{cat} is not available❌')     
    def show_cart(self):
        print("------------DOMINOS CART💻-------------")
        if self.cart!={}:
            total_bill=0
            for item in self.cart:
                total_bill+=self.cart[item]
                print(item,'----------------Rs.',self.cart[item])
            print("Total Bill:............Rs.",total_bill)
        else:
            print("Cart is empty please order......")

        ch=input("Do you want to place order? (y/n):").lower()
        if ch=='y':
            print("Thank you for placing  the order...😍🫶🏻👍🏻")
            print("Your order is on the way...🏍️")
            self.cart={}

    def Logout(self):
        ch=input("Do you want to Logout (y/n):").lower()
        if ch=='y':
            self.login_status=False
            print("Logged out.✅")
ob=Dominos("kaavi","mnkajp@gmail.com",9500654316)     