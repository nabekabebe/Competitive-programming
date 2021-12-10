class Solution:
    def sortSentence(self, s: str) -> str:
        arr  = s.split()

        lst = [0]*len(arr)
        for i in arr:
            lst[int(i[-1])-1] = i[:-1] 


        return " ".join(lst)

