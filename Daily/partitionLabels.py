class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        l_o = {}
        for i, v in enumerate(s):
            l_o[v] =  i

        count = 0 
        ans = []
        while count < len(s):
            start = count
            val = s[count]
            end = l_o[val]
            while count < end:
                end = max(l_o[s[count]], end)
                count += 1
            ans.append(end - start + 1)
            count = end + 1
            
        return ans
