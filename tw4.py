import sqlite3

conn = sqlite3.connect("products.db")
cursor = conn.cursor()

cursor.execute('create table if not exists products(prodID integer primary key ,name text,quantity integer,price real)')

def insert():
    n=int(input("Enter the number of records: "))
    for i in range(n):
        prodID = int(input("Enter the ID - "))
        name = input("Enter the name: ")
        q = int(input("Enter the quantity: "))
        p=float(input("Enter the price: "))
        cursor.execute('insert into products values(?,?,?,?)',(prodID,name,q,p))
        conn.commit()

def display():
    cursor.execute('select * from products')
    records = cursor.fetchall()
    for record in records:
        print(record)

def delete():
    prodID=int(input("Enter id - "))
    cursor.execute('delete from products where prodID = ?',(prodID,))
    conn.commit()
    print("Product deleted successfully!!")

def increase_price():
    cursor.execute('update products set price = 1.1*price where price<50')
    conn.commit()
    print("Prices increased for eligible products!!")

def disLowQP():
    cursor.execute('select * from products where quantity<40')
    records = cursor.fetchall()
    for record in records:
        print(record)

while True:
    print('Menu')
    print("1.insert")
    print("2.display")
    print("3.delete")
    print("4.increase price")
    print("5.display quantity")
    print("6.exit")
    choice=int(input("Enter the choice: "))
    if choice == 1:
        insert()
    elif choice == 2:
        display()
    elif choice == 3:
        delete()
    elif choice == 4:
        increase_price()
    elif choice == 5:
        disLowQP()
    elif choice == 6:
        break