## SINGLY-LINKED-LIST ##

class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:

    def __init__(self) -> None:
        self.head = None


    def insertAtBegin(self, val) -> None:
        """
        Method to insert a new node 
        at the beginning of the linked list
        """
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
        current_node = self.head

        while (current_node != None and
               current_node.next.val != val):
            current_node = current_node.next

        if current_node == None:
            return
        else:
            current_node.next = current_node.next.next


    def sizeOfLL(self) -> None:
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

class Problem:

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
            n = int(input("Please input your number at postion %s :", i))
            l.append(n)
        return l


    def listInputStr(self) -> list[str]:
        l = list()
        listLen = int(input("Please input your list length: "))
        for i in range(listLen):
            n = int(input("Please input your string at postion %s :", i))
            l.append(n)
        return l
    

    def strInput(self) -> str:
        s = input("Please input your string: ")
        return s


class Solution:

    def __init__(self) -> None:
        pass

    def addTwoNumber(self, l1: LinkedList, l2: LinkedList) -> LinkedList:
        """
        Add the two linked list and return the sum as a linked list
        """
        while (l1 and l2):
            l1.head = l1.head.next
            l2.head = l2.head.next
            print("yel it work")
            # if l1.head != None:
            #     l1.head = l1.head.next
            # if l2.head != None:
            #     l2.head = l2.head.next

    
    def splitToLinkedList(self, llistToBeSplit: LinkedList , val: str) -> None:
        """
        Method to split the number into Linked List.
        Example: 1234 -> 1 2 3 4
        with each number represent different node
        """
        for i in val:
            llistToBeSplit.insertAtBegin(i)
            
    
if __name__ == '__main__':

    n1 = Problem().strInput()
    n2 = Problem().strInput()

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    Solution().splitToLinkedList(linked_list_1,n1)
    Solution().splitToLinkedList(linked_list_2,n2)

    result_list = LinkedList()
    result_list = Solution().addTwoNumber(linked_list_1, linked_list_2)
    # result_list.printLL()