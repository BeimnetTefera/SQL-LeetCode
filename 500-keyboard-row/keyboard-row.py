class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        output = []
        
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        
        
        for word in words:
            for i in range(3):
                Yes = True
                if i == 0:
                    for char in word:
                        if char.lower() not in row1:
                            Yes = False
                    if Yes:
                        output.append(word)
                elif i == 1:
                    for char in word:
                        if char.lower() not in row2:
                            Yes = False
                    if Yes:
                        output.append(word)
                elif i == 2:
                    for char in word:
                        if char.lower() not in row3:
                            Yes = False
                    if Yes:
                        output.append(word)
        print(output)
        return output
        
        # p - number of words
        # q - length of longest word
        # 3 - no. of rows
        
        # Time complexity - O(3.p.q) - O(pq)
