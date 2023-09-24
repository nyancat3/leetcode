class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        num_of_one = s.count('1')
        # https://www.geeksforgeeks.org/create-multiple-copies-of-a-string-in-python-by-using-multiplication-operator/
        # Simply using multiplication operator on the string to be copied with the required number of times it should be copied.
        return '1' * (num_of_one - 1) + '0' * (len(s) - num_of_one) + '1'
