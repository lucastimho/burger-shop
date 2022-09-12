# # implement the classes listed below 

# class FoodItem:
#     pass
# class Burger(FoodItem):
#     pass
# class Drink(FoodItem):
#     pass
# class Side(FoodItem):
#     pass
# class Combo(FoodItem):
#     pass
# class Order:
#     def __init__(self, burger, drink, side, combo):
#         self.burger = burger
#         self.drink = drink
#         self.side = side
#         self.combo = combo
#     def order():
#         print("Your Order:")
#         for item in [Order.burger, Order.drink, Order.side, Order.combo]:
#             if item != "no":
#                 print(item.detail)


# def take_order():
#     print("Welcome to Burger Shop")
#     subtotal = 0
#     order_state = True
#     while order_state:

#         # States

#         burger_state = True
#         drink_state = True
#         side_state = True
#         combo_state = True
#         order_check = True
       
#         # Burger

#         b = Burger()
#         while burger_state:
#             burger = input("Do you want a small, medium, or large burger? Type 'no' if you would not like a burger. Type 'q' if you would like to cancel your whole order. ").lower()
#             if burger == "small":
#                 b.detail = burger + " burger"
#                 subtotal += 3
#                 burger_state = False
#             elif burger == "medium":
#                 b.detail = burger + " burger"
#                 subtotal += 4
#                 burger_state = False
#             elif burger == "large":
#                 b.detail = burger + " burger"
#                 subtotal += 5
#                 burger_state = False
#             elif burger == "no":
#                 b.size = burger
#                 burger_state = False
#             elif burger == "q":
#                 burger_state = False
#                 drink_state = False
#                 side_state = False
#                 combo_state = False
#                 order_check = False
#             else:
#                 print("That is not a valid input, please input a valid size.")

#         # Drink

#         d = Drink()
#         while drink_state:
#             drink = input("Do you want a small, medium, or large drink? Type 'no' if you would not like a drink. Type 'q' if you would like to cancel your whole order. ").lower()
#             if drink == "small":
#                 drink_order_status = True
#                 while drink_order_status:
#                     drink_type = input("Would like a Pepsi, Sprite, or Lemonade? ").lower()
#                     if drink_type == "pepsi":
#                         d.type = "Pepsi"
#                         drink_order_status = False
#                     elif drink_type == "sprite":
#                         d.type = "Sprite"
#                         drink_order_status = False
#                     elif drink_type == "lemonade":
#                         d.type = "Lemonade"
#                         drink_order_status = False
#                     else:
#                         print("That is not a valid input, please input a valid drink.")
#                 d.detail = drink + " " + d.type 
#                 subtotal += 1
#                 drink_state = False
#             elif drink == "medium":
#                 drink_order_status = True
#                 while drink_order_status:
#                     drink_type = input("Would like a Pepsi, Sprite, or Lemonade? ").lower()
#                     if drink_type == "pepsi":
#                         d.type = "Pepsi"
#                         drink_order_status = False
#                     elif drink_type == "sprite":
#                         d.type = "Sprite"
#                         drink_order_status = False
#                     elif drink_type == "lemonade":
#                         d.type = "Lemonade"
#                         drink_order_status = False
#                     else:
#                         print("That is not a valid input, please input a valid drink.")
#                 d.detail = drink + " " + d.type
#                 subtotal += 2
#                 drink_state = False
#             elif drink == "large":
#                 drink_order_status = True
#                 while drink_order_status:
#                     drink_type = input("Would like a Pepsi, Sprite, or Lemonade? ").lower()
#                     if drink_type == "pepsi":
#                         d.type = "Pepsi"
#                         drink_order_status = False
#                     elif drink_type == "sprite":
#                         d.type = "Sprite"
#                         drink_order_status = False
#                     elif drink_type == "lemonade":
#                         d.type = "Lemonade"
#                         drink_order_status = False
#                     else:
#                         print("That is not a valid input, please input a valid drink.")
#                 d.detail = drink + " " + d.type
#                 subtotal += 3
#                 drink_state = False
#             elif drink == "no":
#                 d.detail = drink
#                 drink_state = False
#             elif drink == "q":
#                 drink_state = False
#                 side_state = False
#                 combo_state = False
#                 order_check = False
#             else:
#                 print("That is not a valid input, please input a valid size.")

#         # Side

#         s = Side()
#         while side_state:
#             side = input("Do you want a small, medium, or large fries? Type 'no' if you would not like a fries. Type 'q' if you would like to cancel your whole order. ").lower()
#             if side == "small":
#                 s.detail = side + " fries"
#                 subtotal += 1
#                 side_state = False
#             elif side == "medium":
#                 s.detail = side + " fries"
#                 subtotal += 2
#                 side_state = False
#             elif side == "large":
#                 s.detail = side + " fries"
#                 subtotal += 3
#                 side_state = False
#             elif side == "no":
#                 s.detail = side
#                 side_state = False
#             elif side == "q":
#                 side_state = False
#                 combo_state = False
#                 order_check = False
#             else:
#                 print("That is not a valid input, please input a valid size.")


#         # Combo

#         c = Combo()
#         if b.detail == s.detail and b.detail == d.detail:
#             c.detail = b.detail + " combo"
#             if c.detail == "small combo":
#                 subtotal += 4
#             elif c.detail == "medium combo":
#                 subtotal += 7
#             elif c.detail == "large combo":
#                 subtotal += 11
#         else:
#             while combo_state:
#                 combo = input("Do you want a small, medium, or large combo? Type 'no' if you would not like a combo. Type 'q' if you would like to cancel your whole order. ").lower()
#                 if combo == "small":
#                     c.detail = combo + " combo"
#                     subtotal += 1
#                     combo_state = False
#                 elif combo == "medium":
#                     c.detail = combo + " combo"
#                     subtotal += 2
#                     combo_state = False
#                 elif combo == "large":
#                     c.detail = combo + " combo"
#                     subtotal += 3
#                     combo_state = False
#                 elif combo == "no":
#                     c.detail = combo
#                     combo_state = False
#                 elif combo == "q":
#                     combo_state = False
#                     order_check = False
#                 else:
#                     print("That is not a valid input, please input a valid size.")

#         order_check = input("Would you like to add to your order? (y/n) ").lower()
#         while order_state:
#             if order_check == "n":
#                 order_state = False
#                 print("Thank you for visiting Burger Shop!")
#                 print("Your subtotal is $" + str(subtotal))
#             elif order_check == "y":
#                 print("Okay let's add to your order.")
#                 break
#             else:
#                 print("That is not a valid input, please try again")
        
        
            
# take_order()

#The food_item class
class food_item:
 def __init__(self,name,price): #initializes the values of our food item.
    self.name = name
    self.price = price
 def __str__(self): #creates the string representation of an object derived from the food_item class. 
    return "Item: " + self.name + "\n" + "Price: $" + str(self.price) + "\n"
 def get_price(self):                       #returns the price of the food item.
    return self.price


#The burger class
class burger(food_item):
    def __init__(self,name,price):
        super(burger, self).__init__(name,price)
        self.condiments = []   #initializes the condiments list to empty
    def add_condiment(self,condiment):
        if condiment not in self.condiments:
            self.condiments.append(condiment)
    def __str__(self):
        s = super(burger, self).__str__()
        s = s + "Condiments:" + ", ".join(self.condiments)
        return s


#The drink class
class drink(food_item):
    def __init__(self,name,size,price):
        super(drink, self).__init__(name,price)
        self.size= size
    def __str__(self):
        s = super(drink, self).__str__()
        s = s + "Size: " + str(self.size) + "oz"
        return s


#the side class
class side(food_item):
    def __init__(self,name,price):
        super(side, self).__init__(name, price)


#The combo class
class combo(food_item):
    def __init__(self,name,b,d,s,discount):
        self.name = name
        self.burger = b
        self.drink = d
        self.side = s
        self.discount = discount
        self.price = self.burger.get_price() + self.drink.get_price() + self.side.get_price() - self.discount
    def __str__(self):
        s = ""
        s = s + "Combo: " + self.name + "\n"
        s = s + str(self.burger) + "\n" + str(self.drink)+ "\n" + str(self.side)+ "\n"
        s = s + "Combo Price Before Discount: $" + str(self.burger.get_price()+self.drink.get_price()+self.side.get_price())+ "\n"
        s = s + "Discount: $" + str(self.discount)+ "\n"
        s = s + "Combo Price After Discount: $" + str(self.price)+ "\n"
        
        return s

#Here, we include a burger, a drink, and a side, add together the separate prices of each item, and apply a discount.
#The result is the list of items in the combo and the final price of the combo.

#This class sets up a new order with the following properties:
#It includes a name property that identifies (or names) the order.
#It creates a new empty list named items that will hold the items in the order.
#It gets the price for each item and adds that price to the total price for the order.
#It joins the individual items in the item list into a new string that it can display to the customer.
#We also define a series of output statements to the customer, including their name, a complete list of the items ordered, and the total price.

#The order class
class order:
   def __init__(self,name):
      self.name = name
      self.items = []
   def add_item(self,item):
      self.items.append(item)
   def get_price(self):
      price = 0.0
      for item in self.items:
         price = price + item.get_price()
      return price
   def __str__(self):
      s = [str(item) for item in self.items]
      return "\n".join(s)
   def display(self):
      print("==========================================")
      print("Here is a summary of your order")
      print("Order for " + self.name)
      print("Here is a list of items in the order")
      
      for item in self.items:
         print("-----------")
         print(str(item))
         print("-----------")
         print("Total Order Amount :$" + str(self.get_price()))
         print("==========================================")

BURGER_PRICE = 6.00
BURGER_CONDIMENTS = ["tomato","lettuce","onion","cheese"]

DRINK_TYPES = ["fanta", "coca cola", "sprite"]
DRINK_SIZES = [12, 16, 20]
DRINK_PRICES = [1.00,2.00,3.00]

SIDE_PRICE = 3.00
SIDES = ["fries","coleslaw","salad"]

COMBO_DISCOUNT = 2.00

#Getting a burger order
    #Asks the customer what condiments they want on their burger.
def get_burger_order():  
    b = burger("Burger",BURGER_PRICE)
    q1 = input("Do you want any condiments on your burger? (y for yes) ")
    if q1.lower() =="y":
        for condiment in BURGER_CONDIMENTS:
            q = input("Do you want " + str(condiment)+"? (y/n): ")
            if q.lower() == "y":
                b.add_condiment(condiment)
    return b


#Adding a drink
#This code shows the customer the available drink options and sizes and then prompts the customer to enter their choices.
def get_drink_order():
    print("These are the available drinks:")
    print(DRINK_TYPES)
    print("These are the available sizes:")
    print(DRINK_SIZES)
    choice = False
    drink_name = None
    drink_size = None
    drink_price = None
    while choice == False:
        q1 = input("What drink do you want? ")
        if q1.lower() in DRINK_TYPES:
            choice = True
            drink_name = q1.lower()
        else:
            print("Please enter a valid drink.")
    choice = False
    while choice == False:
        q1 = input("What size do you want? " + str(DRINK_SIZES) + ": ")
        if int(q1) in DRINK_SIZES:
            choice = True
            drink_size = int(q1)
        else:
            print("please enter a valid size")
    drink_price = DRINK_PRICES[DRINK_SIZES.index(drink_size)] #locate the price of the drink based on the index of the size
    d = drink(drink_name,drink_size,drink_price)
    return d


#Adding a side order
#will prompt the customer for their choice of side and return the value with its price.
def get_side_order():
    print("These are the available sides:")
    print(SIDES)
    choice = False
    side_name = None
    while choice == False:
        q1 = input("What side do you want? ")
        if q1.lower() in SIDES:
            choice = True
            side_name = q1.lower()
        else:
            print("Please enter a valid side.")
    s = side(side_name,SIDE_PRICE)
    return s


#Getting a combo
#The COMBO_DISCOUNT constant so that the customer gets the discount, and it passes the result to order_once, 
# which passes it to order_many to add to the order total.
def get_combo_order():
    print("Let's get you a combo meal!")
    print("First, let's order the burger for your combo.")
    b = get_burger_order()
    print("Now, let's order the drink for your combo.")
    d = get_drink_order()
    print("Finally, let's order the side for your combo.")
    s = get_side_order()
    c = combo("Combo",b,d,s,COMBO_DISCOUNT)
    #print(str(c))
    return c




#Creating an order once
#Here, we present the customer with a list of items that they can choose from by entering a number to represent the item they want to order. The list possible_options is used to assign a value to each of the menu items.
#We initialize choice and item as empty variables so that we can add values to those variables as we look through the choices.
#then include a while loop that prompts the customer for an item as long as no valid choice has been entered.

def order_once(): #Identifies a single item for the customer's order. If the customer orders a burger (as in our code so far), it triggers the get_burger_order function.
    possible_options = [1,2,3,4]
    print("Type 1 for a Burger.")
    print("Type 2 for a Drink.")
    print("Type 3 for a Side.")
    print("Type 4 for a Combo.")
    choice = None
    while choice == None:
        q1 = input("Please enter your choice:")
        if int(q1) in possible_options:
            choice = int(q1)
    item = None
    if choice == 1:
        item = get_burger_order()
    elif choice == 2:
        item = get_drink_order()
    elif choice == 3:
        item = get_side_order()
    elif choice == 4:
        item = get_combo_order()
    return item



#creating an order
# It greets the customer and asks for their name. That name is stored in the variable o# as part of order.
#It creates a loop that allows the customer to request one item at a time until they complete the order. 
#Each item is stored in an item list using the add_item function.
#It returns the complete order


def order_many(): #Greets the customer and creates the order. It also creates an item list that will store the output from order_once.
    print("Welcome to Mary's Burger Shop!")
    q1 = input("May I have your name for the order? ")
    o = order(q1)
    print("Let's get your order in!")
    done = True
    while done:
        item = order_once()
        o.add_item(item)
        q1= input("Do you need more items? (Enter n to stop.) ")
        if q1.lower()=="n":
            done = False
    return o


#we want our program to print out what the customer ordered, along with the total price. 
#Right now, this is all stored in the order_many function (including the initial greeting to the customer), 
#so we want to take the output from that function and display it to the customer.
client_order = order_many() 
client_order.display()