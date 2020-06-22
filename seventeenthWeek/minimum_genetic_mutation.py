class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        gene_len = len(start)
        possible_dict = collections.defaultdict(list)
        for gene in bank:
            for i in range(gene_len):
                possible_dict[gene[:i]+'#'+gene[i+1:]].append(gene)
                
        queue = collections.deque([(start, 1)])
        visited = {start}
        while queue:
            cur_gene, mutations = queue.popleft()
            for i in range(gene_len):
                to_gene = cur_gene[:i] + '#' + cur_gene[i+1:]
                for word in possible_dict[to_gene]:
                    if word == end:
                        return mutations
                    if word not in visited:
                        queue.append((word, mutations+1))
                        visited.add(word)
                possible_dict.pop(to_gene)
        return -1
    