class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:

        val_1 = ''.join(word1)
        val_2 = ''.join(word2)

        return val_1 == val_2