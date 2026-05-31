class Solution(object):
    def recoverOrder(self, order, friends):
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        finish=[]
        for i in range(len(order)):
            if order[i] in friends:
                finish.append(order[i])
        return finish

        
