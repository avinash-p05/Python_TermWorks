class Person:
    def  __init__(self,f,l,e,add):
        self.__f=f
        self.__l=l
        self.__e=e
        self.__add=add
    def getdetails(self):
        return self.__f+" "+self.__l+" "+self.__e+" "+self.__add

class Customer(Person):
    def __init__(self,f,l,e,add,id):
        Person.__init__(self,f,l,e,add)
        self.__id=id
    @property
    def getdetails(self):
        return self.__f+" "+self.__l+" "+self.__e+" "+self.__add+" "+self.__id

class Employee(Person):
    def __init__(self,f,l,e,add,pan):
        Person.__init__(self,f,l,e,add)
        self.__pan=pan
    @property
    def getdetails(self):
        return self.__f + " " + self.__l + " " + self.__e + " " + self.__add + " " + self.__pan

def show(obj):
    if isinstance(obj,Customer):
        print("Customer name , email, address , id is ",obj.getdetails())
    elif isinstance(obj,Employee):
        print("Employee name , email, address , pan is ",obj.getdetails())
    elif isinstance(obj,Person):
        print("Person name , email, address  is ", obj.getdetails())

def main():
    while True:
        print("1.Customer  2.Employee  3.Person    4.Exit")
        choice = int(input("Enter choice- "))
        if choice==1:
            f,l,e,add,id = input("Enter the first name,last name,email,address and id of Customer - ").split()
            c=Customer(f,l,e,add,id)
            show(c)
        elif choice==2:
            f,l,e,add,pan = input("Enter the first name,last name,email,address and pan of Employee - ").split()
            e=Employee(f,l,e,add,pan)
            show(e)
        elif choice==3:
            f,l,e,add = input("Enter the first name,last name ,email and address of person - ").split()
            p=Person(f,l,e,add)
            show(p)
        elif choice==4:
            break

if __name__=='__main__':
    main()