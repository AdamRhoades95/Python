numID = ""
description = ""
quantity = 0
price = 0.00
cart =[]

def Sales (Id, descript, qty, cost):
        global numID, description, quantity, price, cart
        numID = Id
        description = descript
        quantity = qty
        price = cost
        cart.append([numID, description, quantity, price])

def Display():
        counter = 1
        newqty = 0
        total = 0
        for items in cart:
                for item in items:
                        if(counter % 4 == 1):
                                print("\nProduct Info:")
                                print("Item number: "+ str(item))
                        elif(counter % 4 == 2):
                                print("Item number: "+ str(item))
                        elif(counter % 4 == 3):
                                print("Item quantity: "+ str(item))
                                newqty = float(item)
                        elif(counter % 4 == 0):
                                total = total + (item*newqty)
                                print("The price $"+ str(item))
                                print("the total cost for the quantity is $" + str(item*newqty))
                                print("------------------------------------------------")
                        counter = counter + 1
                        
        print("\nthe total before tax is $"+ str(total))

def Shopping():
        Id = 0
        while (Id != "-1"):
                Id = raw_input("enter a id: ")
                print (Id)
                if(Id != "-1"):
                        descript = raw_input("what is the food? ")
                        qty = float(raw_input("enter the quantity: "))
                        cost = float(raw_input("enter the price $"))
                        if (qty < 0):
                                qty = 0
                                cost = 0
                        if (cost < 0):
                                cost = 0
                                qty = 0
                        if (qty != 0):
                                Sales(Id, descript, qty, cost)

#start
Shopping()
Display()



