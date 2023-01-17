import math

#def romanToInt(self, s):
def findRelativeRanks(score):
    if len(score) == 1:
        return ['Gold Medal']
    elif len(score) == 2:
        if score[0] > score[1]:
            return ['Gold Medal' , 'Silver Medal']
        else:
            return ['Silver Medal','Gold Medal' ]
    else:
        top_score = []
        for i in range(len(score)):
            top_score.append([i,score[i]])
        top_score.sort(key=lambda x: x[1], reverse=True)

        res = [0]*len(score)
        for i in range(len(top_score)):
            if i == 0:
                res[top_score[i][0]] = 'Gold Medal'
            elif i == 1:
                res[top_score[i][0]] = 'Silver Medal'
            elif i == 2:
                res[top_score[i][0]] = 'Bronze Medal'
            else:
                res[top_score[i][0]] = i


        return res



score = [10,3,8,9,4]
print(findRelativeRanks(score))

