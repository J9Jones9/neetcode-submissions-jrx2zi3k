class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        my_dict = {}

        for s in strs:
            sorted_str = str(sorted(s))
            if sorted_str in my_dict:
                my_dict[sorted_str].append(s)
            else:
                my_dict[sorted_str] = [s]

        return list(my_dict.values())


