class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        k=[]
        for i in range(len(words)):
            if x in words[i]:
                    k.append(i) 
        return k
