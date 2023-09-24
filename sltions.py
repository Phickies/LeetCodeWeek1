from prblms import LinkedList,ListNode
import random

class Sltions:
    """
    Class for containning written solution method
    """

    def __init__(self) -> None:
        pass

    def estimatePi(self, number_of_point: int) -> float:
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


    def findDuplicate_Hashmap(self, nums: list[int]):
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

            while (curSum > target and leftPointer < len(nums)):
                curSum -= nums[leftPointer]
                leftPointer += 1
            
            if (curSum == target):
                maxLen = max(maxLen,rightPointer - leftPointer + 1)

        if maxLen < 0:
            return maxLen 

        return len(nums) - maxLen


    def romanToInt(self, s: str) -> int:
        """
        Method to convert roman numeral to an integer.
        """

        hashmap = {'I': 1, 
                   'V': 5,
                   'X': 10,
                   'L': 50,
                   'C': 100,
                   'D': 500,
                   'M': 1000}      
        sum = 0
        
        for i in range(len(s)):
            if (i+1<len(s) and hashmap[s[i]] < hashmap[s[i+1]]):
                sum -= hashmap[s[i]]
            else:
                sum += hashmap[s[i]]

        return sum
    

    def isSubsequence(self, s: str, t: str) -> bool:
        """
        A subsequence of a string is a new string that is formed
        from the original string by deleting some (can be none) of
        the characters without disturbing the relative positions of
        the remaining characters.

        Solving by running two pointer checking the array.
        """

        pointerS = 0

        for pointerT in t:
            if pointerT == s[pointerS]:
                pointerS += 1
        if (pointerS == len(t)):
            return True
        return False
    

    def isPalindrome(self, x: float) -> bool:
        """
        Method for checking if the int x is palindrome or not

        Solving by reversing half of the number,
        using the modulo operator.
        """

        if (x < 0 or (x > 0 and x%10 == 0)):
            return False
        
        reversed = 0

        while (x > reversed):

            # Extract the last digit number from x
            lDigit = x%10

            # Add them into reversed
            reversed *= 10
            reversed += lDigit

            # Remove that number
            x -= lDigit
            x /= 10

        if (x < reversed):
            lDigit = reversed%10
            reversed -= lDigit
            reversed /= 10
            if (x == reversed):
                return True
            return False
        else:
            return True


    def longestStrChain(self, words: list[str]):
        """
        Method to return the length of the longest possible word
        chain with words chosen from the given list of words.

        The arrays of words where each word consists of lowercase English letters.

        the predecessor can only insert exactly one letter to the decessor
        """

        hashmap = {}
        value   = {}
        mx = 0

        count = 0

        # Create a matrix
        for i in words:
            l = len(i)

            if (l == 0):
                return 0

            if (mx<l):
                mx = l

            value[i] = 0

            if (l not in hashmap):
                hashmap[l] = []
            hashmap[l].append(i)
        
        # Iterate the matrix from top left to right down
        while (mx-1 in hashmap):

            # Comparing word in each row
            for word1 in hashmap[mx]:
                for word2 in hashmap[mx-1]:

                    pointerWord2 = 0
                    for pointerWord1 in range(len(word1)):
                        if word2[pointerWord2] == word1[pointerWord1]:
                            pointerWord2+=1

                        # Predecessor found when value of pW2 equal to lW1-1
                        # If found predecessor, value of that num +1
                        if pointerWord2 == len(word1)-1:
                            value[word2] = max(value[word2], value[word1]+1)
                            break
                        
                    # Update the max max of that num
                    count = max(count, value[word2])
            
            mx-=1
        return [hashmap, value, count+1]

    
    def longestStrChain_Answer(self, words: list[str]) -> int:
        """
        Alternative method for the longestStrChain function
        """

        words.sort(key=len)
        dp = {}
        max_chain = 0
        
        for word in words:
            dp[word] = 1

            for i in range(len(word)):
                prev_word = word[:i] + word[i+1:]

                if prev_word in dp:
                    dp[word] = max(dp[word], dp[prev_word] + 1)

            max_chain = max(max_chain, dp[word])

        return max_chain
    

    def champagneTower(self, poured, query_row, query_glass) -> float:
        """
        Method to return how full the glass in the position of the pyramid glass

        Solved by using Simulation method, some might use dp?
        """
        A = [[0] * k for k in range(1,102)]
        A[0][0] = poured

        for r in range(query_row + 1):
            for c in range(r+1):
                q = (A[r][c] - 1.0) / 2.0
                if q > 0:
                    A[r+1][c] += q # type: ignore
                    A[r+1][c+1] += q #type: ignore

        return min(1,A[query_row][query_glass])

    
    def getMin(self, nums1: list[int], nums2: list[int], p1: int, p2: int) -> int:
        """
        Method get the smaller value between nums1[p1] and nums2[p2]
        and move the pointer forward
        """

        return 1

    

    def findMedianSortedArrays_MergeSort(self, nums1: list[int], nums2: list[int]) -> float:
        """
        Method to find the median of the two sorted array

        Solving by using Merge Sort
        """

        return 1