class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = set()

        def backtrack(i, w):
            if i == len(s):
                val = "".join(w)
                ans.add(val)
                return

            if s[i].isalpha():
                for c in [s[i].upper(), s[i].lower()]:
                    w.append(c)
                    backtrack(i+1, w)
                    w.pop()
            else:
                w.append(s[i])
                backtrack(i+1, w)
                w.pop()

        backtrack(0, [])
        return ans
