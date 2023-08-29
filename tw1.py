queue=[]
def enqueue():
    a =int(input("Enter the element: "))
    queue.append(a)
def dequeue():
    if queue==[]:
        print("Queue is empty!!")
    else:
        b=queue.pop(0)
        print("The removed element is : ",b)
def queuefront():
    if queue==[]:
        print("Queue is empty!!")
    else:
        print("The Queue front is ",queue[0])
def queuerear():
    if queue==[]:
        print("Queue is empty!!")
    else:
        n = len(queue)
        print("The Queue Rear is ",queue[n-1])
def display():
    if queue==[]:
        print("Queue is empty!!")
    else:
        for item in queue:
            print(item,end=" ")
        print()










def main():
  while True:
    print("1.ENQUEUE    2.DEQUEUE   3.QUEUE FRONT   4.QUEUE REAR    5.DISPLAY    6.EXIT")
    choice = int(input("Enter the choice: "))
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        queuefront()
    elif choice==4:
        queuerear()
    elif choice==5:
        display()
    elif choice==6:
        break

if __name__=='__main__':
    main()