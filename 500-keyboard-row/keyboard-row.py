class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        output = []
        
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        for word in words:
            count_1 = 0
            count_2 = 0
            count_3 = 0
            for char in word.lower():
                if char in row1:
                    count_1 += 1
                elif char in row2:
                    count_2 += 1
                else:
                    count_3 += 1
            
            if len(word) in [count_1, count_2, count_3]:
                output.append(word)

        return output