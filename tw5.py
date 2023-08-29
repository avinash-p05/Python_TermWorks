class Customer:
    def __init__(self, name, email):
        self.__name = name  # private name
        self.__email = email  # private email
        self.orders = []  # list to store customer orders

    def placeOrder(self, order):
        self.orders.append(order)  # order is an object.Add the given order to orders list

    def getOrders(self):
        return self.orders  # returns list of customer's orders

    def getName(self):
        return self.__name  # getter method to access private name

    def getEmail(self):
        return self.__email  # getter method to access private email


class Order:
    def __init__(self, orderId, products):
        self.__orderId = orderId  # order ID(private)
        self.products = products  # list of products in the orders

    def getOrderId(self):
        return self.__orderId  # getter method to access private orderId

    def getTotalPrice(self):  # calculate the total price of products
        totalPrice = 0
        for product in self.products:
            totalPrice += product.getPrice()
        return totalPrice


class Product:
    def __init__(self, name, price):
        self.__name = name  # private product name
        self.__price = price  # private product price

    def getName(self):
        return self.__name  # getter method to access private product name

    def getPrice(self):
        return self.__price  # getter method to access private product price


# Creating objects
noOfCusts = int(input("Enter the no of Customers: "))
Custs = []
for i in range(noOfCusts):
    name = input('Enter name for Customer ' + str(i + 1) + ': ')
    email = input("Enter the email - ")
    Cust = Customer(name,email)  # Customer instantiation
    Custs.append(Cust)

    noOfOrders = int(input('Enter no of Orders for Customer ' + name + ': '))
    for j in range(noOfOrders):
        oId = int(input('Enter order id for customer ' + name + ': '))
        Prods = []
        noOfProds = int(input('Enter no of products for order ' + str(oId) + ' for Customer ' + name + ': '))
        for k in range(noOfProds):
            pName, price = input('Enter name and price of product: ').split()
            price = float(price)
            Prod = Product(pName, price)  # Product Instantiation
            Prods.append(Prod)
        order = Order(oId, Prods)  # Order instantiation
        Cust.placeOrder(order)
print('\nDetails of Customer orders:')
for cust in Custs:
    # accessing customer information using the getter methods
    print('Customer Name:', cust.getName())
    print('Customer Email:', cust.getEmail())
    # accessing order information
    orders = cust.getOrders()
    for order in orders:
        print('Order ID:', order.getOrderId())
        print('Products:')
        for product in order.products:
            print(product.getName(), 'Rs', product.getPrice())
        print('Total price:', order.getTotalPrice())
        print()