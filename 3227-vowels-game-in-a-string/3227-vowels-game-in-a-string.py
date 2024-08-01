class Solution(object):
    def doesAliceWin(self, s):
        for element in range(0, len(s)):
            if s[element] == "a" or s[element] == "e" or s[element] == "i" or s[element] == "o" or s[element] == "u":
                return True
        return False
        