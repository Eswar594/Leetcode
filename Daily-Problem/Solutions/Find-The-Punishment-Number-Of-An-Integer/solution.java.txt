class Solution {
    public int punishmentNumber(int n) {
        int pn = 0;
        for(int i = 1;i <= n ;i++){
            int sq = i*i;
            
            if(canPartition(sq,i))
              pn += sq;
        }

        return pn;

    }
    public boolean canPartition(int num, int val){
        //invalid
        if(num < val || val < 0)
          return false;

        if(num == val)
          return true;

        return (canPartition(num/10,val-(num%10)) || canPartition(num/100,val-(num%100)) || canPartition(num/1000,val-(num%1000)));
    }
}