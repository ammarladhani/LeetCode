class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def simplifiedFractions(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        returnList = []
        for i in range(2, n + 1):
            for j in range(1, i):
                if self.gcd(j, i) == 1:
                    returnList.append("{}/{}".format(j, i))
        return returnList
