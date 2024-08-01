class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        r = s.split(' ')
        newString = ''
        for i, string in enumerate(r):
            if i + 1 >= k:
                newString += string
                break
            newString += string
            newString += ' '
        return newString
        