class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        k=0
        for word in words:
            if all(char in allowed for char in word):
                k=k+1
        return k
        