def countingValleys(steps, path):
    # Write your code here
    count = 0
    result = 0
    pre = 0
    for i in range(steps):
        if path[i] == 'U':
            pre =result
            result += 1    
        else:
            result -= 1
        if result == 0 and pre == -1:
            count += 1
    return count
