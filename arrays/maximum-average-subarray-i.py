# Maximum Average Subarray I
# Difficulty: Easy
# Category: Array, Sliding Window

"""
    Problem: We're given an array which has n elements and an integer k.
    We need to find a contiguous subarray whose length is equal to k that has the maximum average value and return it.

    e.g:
    Input: nums = [1,12,-5,-6,50,3], k = 4
    Output: 12.75000
    Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

    Approach:
    Use a sliding window because conseutive windows overlap.

    1. First we need to calculate the sum of the first window. (current_sum = sum(nums[:k]))
    2. Next we need to intialise the maximum sum, because the first window is the only one we've seen we make it the max sum.
    3. We slide the window across the array.
    4. We then update the windows's sum.
    5. We then update the max sum
    6. Return the maximum average.

    Time Complexity: O(n)
    Space Complexity: O(1)

    The time complexity of this approach is O(n) because we run the for loop O(k) + O(n - k) times.
    The space complexity of this approach is O(1) because we don't use extra memory we just use the current_sum and max_sum variables no data structures grow with the size.

"""

def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        current_sum = sum(nums[:k])
        max_sum = current_sum

        for i in range(k, len(nums)):
            current_sum = current_sum - nums[i - k] + nums[i]
            max_sum = max(max_sum, current_sum)
        
        return max_sum / float(k)