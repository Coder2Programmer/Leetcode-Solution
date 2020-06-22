class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        gene_dict = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        once_set, twice_set = set(), set()
        for i in range(len(s)-9):
            value = 0
            for j in range(i, i+10):
                value = (value | gene_dict[s[j]]) << 2
            if value in once_set:
                twice_set.add(s[i:i+10])
            once_set.add(value)
            
        return list(twice_set)