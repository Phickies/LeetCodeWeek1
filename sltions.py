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

        # Create a dummy head to keep track of the LinkedList
        dummy_head = l3.head

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

            new_node = ListNode(last_num)
            l3.head.next = new_node
            l3.head = l3.head.next
 
            l1.head = l1.head.next if l1.head is not None else None
            l2.head = l2.head.next if l2.head is not None else None
        
        # Assign the preferencce back to the first node
        l3.head = dummy_head.next

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

    
    def findDuplicate_fastSlow(self, nums: list[int]) -> int:
        """
        Method to find one repeated number in array nums,
        return this repeated number.

        Using the Floyd Cycle Algorithms
        The slow fast pointer way
        """

        slow = 0 
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if (slow == fast):
                break
        
        slow = 0
        while (slow != fast):
            slow = nums[slow]
            fast = nums[fast]

        return slow


    def findDuplicate_Hashmap(self, nums: list[int]) -> int:
        """
        Method to find one repeated number in arrry nums,
        return this repeated number.

        Using the Set/Hashmap to record the occurrence of each number
        
        If the nums is seen then return it
        """

        seen = set()

        for i in nums:
            if (i in seen):
                return i
            seen.add(i)
        return None


    def minOperations(self, nums: list[int], x: int) -> int:
        """
        Method to either remove the leftmost or the rightmost
        element from the array nums and substract its value from x.

        Reduce the minimum number of operations to reduce x to exactly 0
        if it is possible, otherwise, return -1

        Solution using slicing windows technique
        """

        # Calculate the sum of the list
        lSum = 0
        for i in nums:
            lSum += i

        # Subtract with the x to get the target number
        # Goal is to find the unecessary number
        target = lSum - x
        
        # If target == 0, it means that the list is 
        # perfect and meet the condition.
        if (target == 0):
            return len(nums)
        
        # Create tracking pointer
        leftPointer = 0

        curSum = 0
        maxLen = -1
        
        for rightPointer in range(len(nums)):
            
            curSum += nums[rightPointer]

            while (curSum > target):
                curSum -= nums[leftPointer]
                leftPointer += 1
            
            if (curSum == target):
                maxLen = max(maxLen,rightPointer - leftPointer + 1)

        if maxLen < 0:
            return maxLen 

        return len(nums) - maxLen