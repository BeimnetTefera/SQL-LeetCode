class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        mismatch = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                mismatch.append([s1[i], s2[i]])
            if len(mismatch) > 2:
                return False

        if len(mismatch) == 0:
            return True
        if len(mismatch) == 2:
            if mismatch[0][0] == mismatch[1][1] and mismatch[0][1] == mismatch[1][0]:
                return True
        return False