class Solution {
    public List<String> letterCombinations(String digits) {
        LinkedList<String> letters = new LinkedList<>();
        if (digits == null || digits.isEmpty()) {
            return letters;
        }
        
        String[] digitLetter = new String[]{"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        letters.add("");
        for (int index = 0; index < digits.length(); index++) {
            int digitNumber = Character.getNumericValue(digits.charAt(index));
            while (letters.peekFirst().length() <= index) {
                String currentLetters = letters.pollFirst();
                for (char letter : digitLetter[digitNumber].toCharArray()) {
                    letters.offerLast(currentLetters + letter);
                }
            }
        }
        
        return letters;
    }
}
