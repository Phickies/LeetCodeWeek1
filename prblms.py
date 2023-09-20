class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    """
    class for Linked list
    """

    def __init__(self, intMode = True) -> None:
        self.head = None
        self.intMode = intMode


    def insertAtBegin(self, val) -> None:
        """
        Method to insert a new node 
        at the beginning of the linked list
        """
        if (self.intMode):
            val = int(val)

        new_Node = ListNode(val)

        if self.head is None:
            self.head = new_Node
            return
        else:
            new_Node.next = self.head
            self.head = new_Node


    def insertAtIndex(self, val, index: int) -> None:
        """
        Method to insert a node
        at the given index of the linked list
        """
        if (self.intMode):
            val = int(val)
        
        new_node = ListNode(val)
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtBegin(val)
        else:
            # Iterate through to find the desired index
            # or until nothing
            while (current_node != None and
                   position+1 != index):
                position = position+1
                current_node = current_node.next
            
            # Assign the next val of current_node
            # to the next val of new_node and
            # re-assign the next val of current_node 
            # to the new_node val
            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present")


    def insertAtEnd(self, val) -> None:
        """
        Method inserts a node
        at the end of the linked list
        """
        if (self.intMode):
            val = int(val)
        
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
            return
        
        # make the current_node equal to the head
        # traverse to the last node of the linked list
        current_node = self.head
        while (current_node.next):
            current_node = current_node.next

        current_node.next = new_node


    def updateNode(self, val, index: int) -> None:
        """
        Method to update the value of a node at 
        a given position in the linked list.
        """
        if (self.intMode):
            val = int(val)
        
        current_node = self.head
        position = 0
        if position == index:
            current_node.val = val
        
        else: 
            while (current_node != None and
                   position != index):
                position = position+1
                current_node = current_node.next
        
            if current_node != None:
                current_node.val = val
            else:
                print("Index not present")


    def removeFirstNode(self) -> None:
        """
        Method which remove the first node
        of the linked list
        """
        if (self.head == None):
            return
        
        self.head = self.head.next


    def removeLastNode(self) -> None:
        """
        Method which remove the last node
        of the linked list
        """
        current_node = self.head

        if (current_node == None):
            return
        
        # Traverse to the second last node
        while (current_node.next.next):
            current_node = current_node.next

        current_node.next = None

    
    def removeAtIndex(self, index: int) -> None:
        """
        Method which remove the node
        at the given index in the linked list
        """
        current_node = self.head
        position = 0

        if (current_node == None):
            return

        if (position == index):
            self.removeFirstNode()
        else: 
            while (current_node.next != None and 
                position != index):
                position = position+1
                current_node = current_node.next
            
            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index not present")
            
            
    def removeNode(self, val) -> None:
        """
        Method removes the node with the given data
        from the linked list
        """
        if (self.intMode):
            val = int(val)
        
        current_node = self.head

        while (current_node != None and
               current_node.next.val != val):
            current_node = current_node.next

        if current_node == None:
            return
        else:
            current_node.next = current_node.next.next


    def sizeOfLL(self) -> int:
        """
        Method to get the current size
        of the linked list
        """
        size = 0
        if (self.head):
            current_node = self.head
            while (current_node):
                size += 1
                current_node = current_node.next
            return size
        else:
            return 0


    def printLL(self) -> None:
        """
        Method to traverse the linked list and
        prints the data of each node
        """
        current_node = self.head
        while (current_node):
            print (current_node.val)
            current_node = current_node.next

class User:
    """
    Class for user input and problems simplifyed
    """

    def __init__(self) -> None:
        pass


    def lenInput(self) -> int:
        val = int(input("Please input your length: "))
        return val


    def intInput(self) -> int:
        val = int(input("Please input your number: "))
        return val
    

    def listInputInt(self) -> list[int]:
        l = list()
        listLen = int(input("Please input your list length: "))
        for i in range(listLen):
            n = int(input("Please input your number at postion " + str(i) + " :"))
            l.append(n)
        return l


    def listInputStr(self) -> list[str]:
        l = list()
        listLen = int(input("Please input your list length: "))
        for i in range(listLen):
            n = int(input("Please input your string at postion " + str(i) + " :"))
            l.append(n)
        return l
    

    def strInput(self) -> str:
        s = input("Please input your string: ")
        return s