# In Progress Trial
import math
def kClosest(points, k: int):     
    lst  = [0] * k
    for i in range(len(points)):
        sqr = math.sqrt((points[i][0])**2 + (points[i][1])**2) 
        if i < k:
            lst[i] = [sqr, points[i]]
        else:
            pre = 0
            check = False
            for j in range(k):
                if sqr < lst[j][0]:
                    if lst[j][0] >= lst[pre][0]:
                        pre += j
                        check = True
            if check:
                lst[pre] = [sqr, points[i]] 
                                  
    return [i[1] for i in lst]
