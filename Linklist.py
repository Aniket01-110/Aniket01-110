#starting with linked list in python
#creating a class for node in SLL
class Node:
    def __init__(self,item=None,next=None): #here item and next are the local variable
        self.item=item #item  object variable created 
        self.next=next  #next  object variable created

class SLL:
    def __init__(self,start=None):
        self.start=start
        
        #To check if list is initially empty or not
    def isempty_(self):
        return self.start==None
        
        #Inseting at start
    def insert_at_start(self,data):

        n=Node(data,self.start)
        self.start=n #Start is now assigned to new node
        
        #Inserting at last
    def insert_at_last(self,data):
        n=Node(data) #as its last next should be none,its bydefault None assigned
            #if nothing is passed , by default value declared above is assigned
        if not self.isempty_():
            temp = self.start
            while temp.next is not None: #traversing till lastnode
                temp=temp.next
            temp.next=n #assigning new Node(n) to the next of the last node
        else:
            self.start=n #if list was empty
        #Searching an element
    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return  None
        #Insert after a given Node
    def insert_after(self,temp,data): #Here we have conisdered that , search operation is performed
    #and we know after which node we have to insert our new Node
        if temp is not None:
        #First creating the new Node that is to be inserted after a given node
            n=Node(data,temp.next)
            temp.next=n
        
         #creating function for printing
    def  print_list(self):
            temp = self.start
            while temp is not None:
                print(temp.item,end=" ")
                temp = temp.next
    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next 
    def delete_last(self):
       if self.start is None:
            pass
       elif self.start.next is None: #only one node present
           self.start = None
       else:
            temp = self.start #Case Only 2 nodes present
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
    def delete_item(self,data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item==data:
                self.start=None
        else: #This case means atleast 2 node is present 
            temp=self.start
            if temp.item==data:
                self.start=temp.next
            else:
                while temp.next is not None: #traversing the entire list
                    if  temp.next.item==data: #found the element to delete
                        temp.next=temp.next.next #deleting by changing the reference of the next
                        break
                    temp=temp.next
                        
                    
        
#driver code 
mylist=SLL()
mylist.insert_at_start(20)
mylist.insert_at_start(10)
mylist.insert_at_last(30)
mylist.insert_after(mylist.search(20),25) # here we have to insert an element after particular element
#so we first enter, after which element we have to insert,by searching and then mention , value of next element
mylist.print_list()
mylist.delete_item(25)
print()
mylist.print_list()
print()