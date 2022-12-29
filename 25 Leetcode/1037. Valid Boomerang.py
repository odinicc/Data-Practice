import math

def isBoomerang( points):
    l1 = pow(pow(points[0][0]- points[1][0],2) +pow(points[0][1]- points[1][1],2),0.5)
    l2 = pow(pow(points[2][0]- points[1][0],2) +pow(points[2][1]- points[1][1],2),0.5)
    l3 = pow(pow(points[2][0]- points[0][0],2) +pow(points[2][1]- points[0][1],2),0.5)
    print(l1,l2,l3)
    print(abs(l1 - l2-l3) ,abs(l1-l3-l2) , abs(l2 -l3-l1))
    if abs(l1 - l2-l3) < 0.00000001 or abs(l1-l3-l2) < 0.00000001 or abs(l2 -l3-l1) <0.0000001:
        return False
    else:
        return True
nums = [[1,1],[2,2],[3,3]]

print(isBoomerang(nums))

