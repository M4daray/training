class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """ """
        prefix = []
        strs = sorted(strs, key=lambda x: len(x))
        for idx,_ in enumerate(strs[0]):
            buffer = []
            for x in strs:
                buffer.append(x[idx])
            if len(set(buffer)) == 1:
                prefix.append(buffer[0])
            else:
                break
            
        prefix = ''.join(prefix)
        return prefix