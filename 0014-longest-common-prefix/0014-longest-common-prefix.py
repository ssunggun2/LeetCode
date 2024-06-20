class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_str = strs[0]
        prefix = ""
        for s in first_str:
            prefix += s
            for e in strs[1:]:
                if not e.startswith(prefix):
                    return prefix[:-1]
        return prefix 

            
                
        