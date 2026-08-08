# Two Sum
# Difficulty: Easy
# Category: Array, Hash Map

"""
    Problem: Given an array of integers called nums and an integer called target.
    Return the indicies of the two numbers which add up to the target

    e.g 
    nums = [2, 7, 11 15] target = 9
    2 + 7 = 9

    nums = [3, 2, 4] target = 6
    3 + 2 = 6

    Approach:

    Use a hash map to store numbers we have already seen, this will make the solution faster than brute force. O(1) lookups

    1. Enumerate through the nums list to get the index amd value
    2. Calculate the complement (target - num)
    3. Check if the complement is already in the hash map
    4. If the complement is already in the hashmap return the two indicies (if complement in seen)
    5. Otherwise store the current number and its index. (seen[num] = i)

"""

def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        seen = {}

        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in seen:
                return [seen[complement], i]
            
            seen[num] = i