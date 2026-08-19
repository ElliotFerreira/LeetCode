# Length of Last Word
# Difficulty: Easy
# Category: String, One Pointer


"""
    Problem: Given a string s that has words and spaces, return the length of the last word in the string.

    Example 1:
    Input: s = "Hello World"
    Output: 5
    Explanation: The last word is "World" with length 5.

    Approach: Use one pointer starting from the right and try to find the first space.

    1. Create a right pointer at the very end of the string.
    2. While the right pointer is >= 0 and its looking at an empty space move it down. (To find a real letter)
    3. Create a length variable to track the length.
    4. While the right pointer >= 0 and we're not looking at a space add 1 to the length and move the pointer down
    5. Return the length

    Time Complexity: O(n)
    Space Complexity: O(1)

    The time complexity of this approach is O(n) because we might have to look through the whole string.
    The space complexity of this approach is O(1) because we don't use any extra memory like data structures just updating variables.

"""

def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        right = len(s) - 1

        while right >= 0 and s[right] == " ":
            right -= 1
        
        
        length = 0

        while right >= 0 and s[right] != " ":
            length += 1
            right -= 1

        return length