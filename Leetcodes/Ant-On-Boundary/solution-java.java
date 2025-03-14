class Solution {
    public int returnToBoundaryCount(int[] nums) {
        int c = 0,s = 0;
        for(int i=0;i<nums.length;i++){
            s += nums[i];
            if(s==0){
                c++;
            }
        }
        return c;
    }
}