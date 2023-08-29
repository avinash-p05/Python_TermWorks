courses ={}
def addcourse():
    code = input("Enter the code: ")
    if code in courses:
        print("Duplicate courses not allowed!!")
        return
    else:
        name=input("Enter the course name: ")
        faculty= input("Enter the faculty name: ")
        n=input("Enter the no of registration: ")
        courses[code]=[name,faculty,n]
        print("Courses are ",courses)
def disAll(courses):
    if courses=={}:
        print("No courses!!")
        return
    print("Courses are : ")
    for code,[name,faculty,n] in courses.items():
        print(code," ",name," ",faculty," ",n)

def disCourse():
    if courses=={}:
        print("No courses!!")
        return
    code = input("Enter the code: ")
    if code in courses:
        print("Course details are: ")
        print(code,courses[code][0],courses[code][1],courses[code][2])
    else:
        print("Course not found with code - ",code)

def highest_reg():
    if courses=={}:
        print("No courses!!")
        return
    reg=[]
    for details in courses.values():
        reg.append(details[2])
    maxreg = max(reg)
    print("The max registration are : ",maxreg)
    print("The course[s] with highest regs are - ")
    for code,[name,faculty,n] in courses.items():
        if maxreg == n:
            print(name)

def main():
    while True:
        print("1.Add course     2. Display All      3.Display Course       4.Highest regs")
        choice = int(input("Enter the choice: "))
        if choice==1:
            addcourse()
        elif choice==2:
            disAll(courses)
        elif choice==3:
            disCourse()
        elif choice==4:
            highest_reg()
        else :
            print("Invalid!!")

if __name__=='__main__':
    main()