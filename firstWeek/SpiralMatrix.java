class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> traversalSequence = new ArrayList<>();
        if (matrix == null || matrix.length <= 0) {
            return traversalSequence;
        }
        
        int upperBorder = 0;
        int bottomBorder = matrix.length;
        int leftBorder = 0;
        int rightBorder = matrix[0].length;
        while (upperBorder < bottomBorder && leftBorder < rightBorder) {
            for (int i = leftBorder; i < rightBorder; i++) {
                traversalSequence.add(matrix[upperBorder][i]);
            }
            upperBorder++;
            
            for (int i = upperBorder; i < bottomBorder; i++) {
                traversalSequence.add(matrix[i][rightBorder-1]);
            }
            rightBorder--;
            
            if (upperBorder >= bottomBorder) {
                break;
            }
            for (int i = rightBorder - 1; i >= leftBorder; i--) {
                traversalSequence.add(matrix[bottomBorder-1][i]);
            }
            bottomBorder--;
            
            if (leftBorder >= rightBorder) {
                break;
            }
            for (int i = bottomBorder - 1; i >= upperBorder; i--) {
                traversalSequence.add(matrix[i][leftBorder]);
            }
            leftBorder++;
        }
        return traversalSequence;
    }
}
