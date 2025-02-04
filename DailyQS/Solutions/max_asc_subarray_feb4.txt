class Solution {
    public int maxAscendingSum(int[] nums) {
        int a = nums[0],b = nums[0];
        for(int i=0;i<nums.length-1;i++){
            if(nums[i] < nums[i+1]){
                a = a + nums[i+1];
            }
            else{
                a = nums[i+1];
            }
            b = Math.max(a,b);
        }
        return b;
    }
}