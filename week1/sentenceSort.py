class Solution:
    def sortSentence(self, s: str) -> str:
        arr  = s.split()

        for i in range(len(arr)):
            for j in range(len(arr)-1):
                if int(arr[j][-1]) > int(arr[j+1][-1]):
                    arr[j+1], arr[j] = arr[j], arr[j+1]
        no_num = [i[:-1] for i in arr]


        result  = ' '.join([i[:-1] for i in arr])

        return result

