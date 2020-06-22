class Solution {
    public int[][] merge(int[][] intervals) {
        if (intervals == null || intervals.length <= 1) {
            return intervals;
        }
        
        Arrays.sort(intervals, (intervalOne, intervalTwo) -> Integer.compare(intervalOne[0], intervalTwo[0]));
        List<int[]> intervalList = new ArrayList<>();
        int[] currentInterval = intervals[0];
        for (int[] interval : intervals) {
            if (interval[0] <= currentInterval[1]) {
                currentInterval[1] = Math.max(interval[1], currentInterval[1]);
                continue;
            }
            intervalList.add(currentInterval);
            currentInterval = interval;
        }
        intervalList.add(currentInterval);
        return intervalList.toArray(new int[intervalList.size()][]);
    }
}
