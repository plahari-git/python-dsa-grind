class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        a,b="",""
        for i in range(len(word1)):
            a+=word1[i]
        for i in range(len(word2)):
            b+=word2[i]
        return a==b

        