class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        cur_gas = 0
        min_index, min_gas = -1, 0xFFFFFFFF
        for i in range(len(cost)):
            cur_gas += gas[i]
            cur_gas -= cost[i]
            if cur_gas < min_gas:
                min_gas = cur_gas
                min_index = (i + 1) % len(cost)

        return min_index
        