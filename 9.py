class Solution:
    def isPalindrome(self, x: int) -> bool:
        """ """
        copy = str(x)
        reverse = copy[::-1]
        for idx, _ in enumerate(copy):
            if copy[idx] != reverse[idx]:
                return False
        return True