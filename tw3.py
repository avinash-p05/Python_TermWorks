import csv
book=[]
def addbooks():
    n = int(input("Enter the no. of books: "))
    for i in range(n):
        bno = int(input("Enter the book no: "))
        title = input("Enter the title : ")
        author = input("Enter the author: ")
        price = float(input("Enter the price: "))
        book.append([bno,title,author,price])
    with open("books.csv","w",newline='') as file:
        writer = csv.writer(file)
        writer.writerows(book)

def s_by_author():
    flag=0
    author = input("enter the author to search: ")
    with open("books.csv",newline='') as file:
        reader = csv.reader(file)
        for line in reader:
            if author == line[2]:
                flag=1
                if flag==1:
                    print("The book details are - ",line)
        if flag==0:
            print("No books found!!")

def s_by_price():
    flag=0
    try:
        price = float(input("Enter the price to search: "))
        if price<0:
            raise ValueError("Price should be greater than zero!!")
    except ValueError as e:
        print(e)
        return
    with open("books.csv",newline='') as file:
        reader = csv.reader(file)
        for line in reader:
            if price>= line[3]:
                flag=1
                print("The book details are: ",line)
        if flag==0:
            print("No books found!! below or equal to price ",price)

def s_by_title():
    flag=0
    title = input("Enter the title: ")
    with open("books.csv",newline='') as file:
        reader = csv.reader(file)
        for line in reader:
            if title in line[1]:
                flag=1
                print("Books details are ",line)
        if flag==0:
            print("No books found with title : ",title)

def main():
    addbooks()
    print("Books are  - ")
    with open("books.csv","r",newline='') as file:
        reader = csv.reader(file)
        for line in reader:
            print(line)
    while True:
        print("1.Search by author.      2. Search by Price.     3.Search by Title.      4.Exit")
        choice = int(input("Enter the choice: "))
        if choice == 1:
            s_by_author()
        elif choice == 2:
            s_by_price()
        elif choice == 3:
            s_by_title()
        elif choice == 4:
            break

if __name__=="__main__":
    main()


