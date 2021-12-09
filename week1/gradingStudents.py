def gradingStudents(grades):
    # Write your code here
    lst  = []
    for i in grades:
        if i <  38:
            lst.append(i)
        else:
            num = i // 5
            com = (num+1)* 5
            if (com - i) >= 3:
                lst.append(i)
            else:
                lst.append(com)
    return lst
