# Valid Palindrome
# Difficulty: Easy
# Category: Two Pointers, String

"""
    Problem: A phrase is a palindrome if after converting all the uppercase letters into lower case letters and removing the alphanumeric characters
    it reads the same forward and backwards.

    Given a string s, we must determine if it's a palindrome and return True if it is otherwise return False.

    e.g:
    Input: s = "A man, a plan, a canal: Panama" Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

    Empty strings after removing alphanumeric characters are also still palindromes.

    Approach:
    Use two pointers at the opposite ends, check each opposite index while they're still alphanumeric characters.

    1. Initialize a left pointer at the starting index and a right pointer at the final index.
    2. Check while left is right and if it is not an alphanumerical number move  the left forward or right backward.
    3. When you actually get to compare, lower the characters and if the left and right lowered are not equal return false it isn't a palindrome
    4. Increase left by 1 index, decrease right by 1 index.

    If you break out of the loop when left and right cross then you can return true, it's a palindrome.

    Time Complexity: O(n)
    Space Complexity: O(1)

    The time complexity of this approach is O(n) because each character is visited at most once by the pointers
    The space complexity of this approach is O(1) because you don't use extra space you just use variables no arrays, no hashmaps, no strings.
"""

def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1

        while left < right:

            while left < right and not s[left].isalnum():
                left += 1
            
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True