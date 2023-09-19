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

        carry = 0
        l3 = LinkedList(intMode=True)
        l3.head = ListNode()

        # Traverse the linked list, the val is None then assign to 0
        while (l1.head or l2.head or carry != 0):
            
            # Assign fake value if there is no node
            l1_val = l1.head.val if l1.head is not None else 0
            l2_val = l2.head.val if l2.head is not None else 0

            # Sum the two value from two linked list
            current_sum = l1_val + l2_val + carry
            # Caculate the remaining number
            carry       = current_sum // 10
            # This is the number that show
            last_num    = current_sum % 10

            l3.insertAtEnd(last_num)
 
            l1.head = l1.head.next if l1.head is not None else None
            l2.head = l2.head.next if l2.head is not None else None
        
        l3.head = l3.head.next

        return l3



    def splitToLinkedList(self, 
                          llistToBeSplit: LinkedList , 
                          val
                          ) -> None:
        """
        Method to split the string into Linked List.
        Example: 1234 -> 1 2 3 4
        with each char represent different node
        """
        for i in val:
            llistToBeSplit.insertAtBegin(i)