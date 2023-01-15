# Shopping Cart Design
class User:
    user_lst = []  # class variable

    def __init__(self, username, password) -> None:
        self.username = username  # instance variable
        self.password = password


class Item:
    def __init__(self, itemID, price, description, quantity):
        self.itemID = itemID
        self.price = price
        self.description = description
        self.quantity = quantity


class ShoppingBasket:
    # {{"name" : "rahat"}}
    user_lst = []
    user_ordered_data = {}
    itemDB = []

    def get_userslst(self):
        return self.user_lst

    def create_account(self):
        name = input("Enter your username: ")
        isNameExist = True  # True mane hocche user already ache
        for user in self.get_userslst():  # user already ache kina seta check
            if user['username'] == name:
                print("Bhai tomar to account kholay ache!!!!!")
                isNameExist = False
                break
        if isNameExist:
            password = input("Enter your password: ")
            self.new_user = User(name, password)
            self.user_lst.append(vars(self.new_user))
            print("Account created successfully.")

    def addItemToCart(self, username):
        itemid = input("Enter Item ID : ")
        quantity = int(input("Enter item quantity : "))
        flag = 0  # item unavailable
        price = 0
        for i in self.itemDB:
            if i['itemID'] == itemid and i['quantity'] >= quantity:
                price = i['price']
                flag = 1  # item available
                break
        if flag == 0:  # item unavailable
            print("Items not available")
        else:  # item available
            if self.user_ordered_data.get(username) == None:
                self.user_ordered_data[username] = []

            self.user_ordered_data[username] += [
                {'itemID': itemid, 'price': price, 'quantity': quantity}]

    def updateProductCart(self, username):
        itemid = input("Enter item ID : ")
        quantity = int(input("Enter updated quantity Number : "))
        for i in self.user_ordered_data[username]:
            if i.get('itemID') == itemid:
                if quantity <= i['quantity']:
                    i['quantity'] += quantity
                else:
                    print("out of stock")
                    break

    def deleteProductCart(self, username, itemid):
        flag = 0  # item unavailable
        for i in self.itemsDB:
            if i['itemID'] == itemid:
                flag = 1  # item available
                print("available")

        if flag:  # item available
            for i in self.user_ordered_data[username]:
                if i["itemID"] == itemid:
                    self.user_ordered_data[username].remove(i)

    def showCart(self, username):
        print("Item ID \t Item Price \t Item Quantity")
        total_price = 0
        if self.user_ordered_data.get(username) is not None:
            for i in self.user_ordered_data[username]:
                print(f"{i['itemID']} \t\t {i['price']} \t\t {i['quantity']} ")
                total_price += i['price'] * i['quantity']
            print("___________________________________________________________")
            print(f"Total Price = {total_price}")
        else:
            print("\nEmpty\n")
    # for admin only
    def addItemToDAtabase(self):# admin product create korben
        itemId = input("Enter itemId: ")
        isItemAvailable = False
        for i in self.itemDB:
            if i['itemID'] == itemId:
                isItemAvailable = True
        
        if isItemAvailable == False:
            description = input(" Enter item description: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity : "))
            self.new_item = Item(itemId, price, description, quantity)
            self.itemDB.append(vars(self.new_item))
        else:
            print("\nitem already added\n1")

    def delProductFromDatabase(self):  # admin product create korben
        itemId = input("Enter itemId: ")
        isItemAvailable = False
        for i in self.itemDB:
            if i['itemID'] == itemId:
                self.itemDB.remove(i)
                print("\nItem Remove Successfully\n")

    def showItemsTable(self):
        print("Item Id \t Item Description \t Item Price \t Item Quantity")
        for i in self.itemDB:
            print(
                f"{i['itemID']}\t\t {i['description']} \t\t\t {i['price']} \t\t\t {i['quantity']}")


basket = ShoppingBasket()

while True:
    print("\n1.Create an Account \n2. Login to YOur Account \n3. EXIT\n")
    user_choice = int(input("Enter your choice : "))

    if user_choice == 3:
        break
    elif user_choice == 1:
        basket.create_account()
    elif user_choice == 2:
        name = input("Enter your name: ")
        password = input("Enter your Password: ")
        isAdmin = 0
        if name == "admin" and password == '123':
            isAdmin = True # se ekjon admin
        if isAdmin == False: # normal user/customer
            isNameExist = False # |True mane hocche amar customer, False mone hoscche fraud
            for user in basket.user_lst:
                if user['username'] == name and user['password'] == password:
                    isNameExist = True
                    break
            if isNameExist: #se hoscce amer customer
                while True:
                    print("\nWelcome to Phitron Shopping Cart")
                    print("\n1. Add item to your cat \n2. Update your cart\n3. Delete your cart\n4. show your cart \n5. Exit\n")
                    choice = int(input("Enter your choice : "))
                    if choice == 1:
                        basket.addItemToCart(name)
                    elif choice == 2:
                        basket.updateProductCart(name)
                    elif choice == 3:
                        item = input("Enter item id : ")
                        basket.deleteProductCart(name, item)
                    elif choice == 4:
                        basket.showCart(name)
                    else:
                        break
        else:
            while True:
                print(f"\nHello Admin, welcome back\n")
                print(f"1.Add New Item \n2. Show Items Table \n3. Delete Item\n4.exit")
                a = int(input("Enter Your Choice : "))
                if a == 5:
                    break
                elif a==1:
                    basket.addItemToDAtabase()
                elif a == 2:
                    basket.showItemsTable()
                elif a== 3:
                    basket.delProductFromDatabase()
                else:
                    break
            