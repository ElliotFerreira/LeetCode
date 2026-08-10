# Contains Duplicate
# Difficulty: Easy
# Category: Array, Hash Table / Set

"""
    Problem: We're given an array of integer called nums, we should return true if an element appears more than once.
    If no elements appear more than once then we should return false.

    e.g
    nums = [1,2,3,1] output = true
    nums = [1,2,3,4] output = false

    Approach:
    Use a hash set to store values that we have seen, this will be faster to lookup values from than an array.

    1. Create a set to store the values we have already seen.
    2. Loop through the nums list and check if an element is already in our seen list.
    3. If it is in our seen list return true.
    4. If it not in our seen list add it to the set.
    5. The loop will iterate again, if it breaks out of the loop we return False because we found no duplicates.


    Time Complexity: O(n)
    Space Complexity: O(n)

    The time complexity of this approach is O(n) because in the worst case we loop through this once.
    The space complexity of this approach is O(n) because int he worst case the set stores every element.


"""
