class Solution {
    public int[] leftRightDifference(int[] nums) {
        int l = 0,r = 0;
        int [] arr = new int[nums.length];
        for(int num:nums){
            r += num;
        }

        for(int i = 0; i<nums.length; i++){
            l += nums[i];
            arr[i] = Math.abs(l-r);
            r -= nums[i];
        }
        return arr;
    }
}