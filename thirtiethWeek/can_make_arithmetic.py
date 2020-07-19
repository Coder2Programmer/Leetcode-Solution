class Solution:
    def canMakeArithmetricProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        return all(n1-n2 == arr[0]-arr[1] for n1, n2 in zip(arr, arr[1:]))
