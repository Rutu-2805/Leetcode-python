class Solution(object):
    def isPalindrome(self, x):
        original = x
        if x < 0 : 
            return False

        reverse = 0
        while x > 0:

            last_digit = x % 10
            x = x // 10
            reverse = reverse * 10 + last_digit

        if original == reverse:
            return True

        else:
            return False

        """
        :type x: int
        :rtype: bool
        """