class Solution {
    public int[] applyOperations(int[] nums) {
        int[] arr = new int[nums.length];
        int c = 0;
        for(int i=0;i<nums.length-1;i++){
            if(nums[i] == nums[i+1] && nums[i]!=0){
                nums[i]*=2;
                nums[i+1] = 0;
            }

        }

        for(int i=0;i<nums.length;i++){
            if(nums[i]!=0){
                arr[c] = nums[i];
                c += 1;
            }
        }

        for(int i=0;i<nums.length-arr.length;i++){
            arr[c] = 0;
            c += 1;
        }

        return arr;
    }
}