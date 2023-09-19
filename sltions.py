from prblms import LinkedList,ListNode
import random

class Sltions:
    """
    Class for containning written solution method
    """

    def __init__(self) -> None:
        pass

    def estimatePi(number_of_point: int) -> int:
        """
        Calculate the PI number with number of given
        point
        """
        point_in_circle = 0
        point_in_total = 0

        for _ in range(number_of_point):
            x = random.uniform(0,1)
            y = random.uniform(0,1)

            distane = x**2 + y**2
            if distane <= 1:
                point_in_circle += 1
            point_in_total += 1

        return float(4*(point_in_circle/point_in_total))


    def addTwoNumber(self, 
                     l1: LinkedList, 
                     l2: LinkedList
                     ) -> LinkedList:
        """
        Add the two linked list and return the sum as a linked list
        """
        n1, n2 = "",""

        new_linked_list = LinkedList(intMode=False)

        while (l1.head): 
            n1 += l1.head.val
            l1.head = l1.head.next
        while (l2.head):
            n2 += l2.head.val
            l2.head = l2.head.next
        self.splitToLinkedList(new_linked_list,str(int(n1) + int(n2)))

        return new_linked_list
        

    
    def splitToLinkedList(self, 
                          llistToBeSplit: LinkedList , 
                          val: str
                          ) -> None:
        """
        Method to split the string into Linked List.
        Example: 1234 -> 1 2 3 4
        with each char represent different node
        """
        for i in val:
            llistToBeSplit.insertAtBegin(i)