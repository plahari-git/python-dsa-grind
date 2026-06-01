class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        n = len(score)
        sorted_score = sorted(score, reverse=True)
        rank_map = {}
        for i in range(n):
            if i == 0:
                rank_map[sorted_score[i]] = "Gold Medal"
            elif i == 1:
                rank_map[sorted_score[i]] = "Silver Medal"
            elif i == 2:
                rank_map[sorted_score[i]] = "Bronze Medal"
            else:
                rank_map[sorted_score[i]] = str(i + 1)
        
        answer = []
        for i in range(n):
            answer.append(rank_map[score[i]])
        return answer

