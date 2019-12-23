class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        mid_index = len(nums) // 2
        root = TreeNode(nums[mid_index])
        root.left = self.sortedArrayToBST(nums[:mid_index])
        root.right = self.sortedArrayToBST(nums[mid_index + 1:])

        return root
