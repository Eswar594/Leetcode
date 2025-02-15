class Solution {
    public int mostWordsFound(String[] sentences) {
        int max = 0;
        for(String i:sentences){
            int l = i.split(" ").length;
            if(max<l) max = l;
        }
        return max;
    }
}