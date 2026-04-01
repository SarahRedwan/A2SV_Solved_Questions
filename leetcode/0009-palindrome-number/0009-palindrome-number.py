class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        number=x
        reverse=0

        while number > 0:
            digit=number%10
            reverse=reverse*10+digit
            number//=10
        return reverse==x


