class Solution {
    public int[] pivotArray(int[] nums, int pivot) {
        int[] res = new int[nums.length];
        int a = 0;
        for (int i : nums) {
            if (i < pivot) {
                res[a++]=i;
            }
        }
        for (int i : nums) {
            if (i == pivot) {
                res[a++] = i;
            }
        }
        for (int i : nums) {
            if (i > pivot) {
                res[a++] = i;
            }
        }
        return res;
    }
}
