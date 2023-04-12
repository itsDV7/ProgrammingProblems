class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ana = {}
        # for s in strs:
        #     cntr = Counter(s)
        #     if cntr in ana.keys():
        #         ana[cntr].append(s)
        #     else:
        #         ana[cntr] = list()
        # ans = []
        # for k,v in ana.items():
        #     ans.append(v)
        # return ans
        
        dct = {}
        for s in strs:
            srt = ''.join(sorted(s))
            if srt in dct:
                dct[srt].append(s)
            else:
                dct[srt] = [s]
        ans = []
        for k,v in dct.items():
            ans.append(v)
        return ans
