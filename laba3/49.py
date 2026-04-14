class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = dict()
        for i in strs:
            a = ''.join(sorted(i))
            
            if a not in s:
                s[a] = [i]
            else:
                s[a].append(i)
        
        return list(s.values())