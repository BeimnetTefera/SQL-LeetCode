class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for sign in operations:
            if sign in ['X++', '++X']:
                x += 1
            else:
                x -= 1
        return x