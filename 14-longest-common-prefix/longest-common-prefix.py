class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        com_prefix = strs[0]

        for word in strs[1:]:

            while not word.startswith(com_prefix):
                com_prefix = com_prefix[: -1]

                if not com_prefix:
                    return ''

        return com_prefix
