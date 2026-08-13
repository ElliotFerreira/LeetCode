# Binary Search
# Difficulty: Easy
# Category: Binary Search

"""
    Problem: Given an array of numbers which is sorted in ascending order, and an integer called target
    write a function to search for target in the list, if it exists return its index otherwise return -1.

    e.g Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4

    Approach:
    1. Initialise a low and high variable, low for the first index of the list, high for the final index of the list.
    2. Create a while loop which runs while low <= high
    3. Calculate the middle of the list (low + high) // 2 (Floor division because if there are two elements in the middle we go for the left one.)
    4. If the lists middle nums[mid] == target then we return it and we're done
    5. If the middle number is less than the target then low = mid + 1 to narrow it down
    6. If the middle number is greater than the target then high = mid - 1 to narrow it down
    7. The loop repeats
    8. If the loop exits and we haven't found it we return -1.

    Time Complexity: O(log n)
    Space Complexity: O(1)

    The time complexity of this approach is O(log n) because we cut the search space in half every time
    The space complexity of this approach is O(1) because the amount of extra memory we use stays constant regardless of how large nums becomes.


"""

def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        low = 0
        high = len(nums) - 1

        while low <= high:

            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                low = mid + 1
            
            else:
                high = mid - 1
        
        return -1