class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        bit = [i.bit_count() for i in range(60)]
        ans = []
        for h in range(12):
            hour = bit[h]
            for m in range(60):
                minute = bit[m]
                if hour + minute == turnedOn:
                    ans.append(f"{h}:{m:02d}")

        return ans
