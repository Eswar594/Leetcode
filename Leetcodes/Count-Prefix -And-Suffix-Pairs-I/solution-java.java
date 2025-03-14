class Solution {
    public int countPrefixSuffixPairs(String[] words) {
        int c = 0;
        int n = words.length;
        for(int i=0;i<n;i++){
            for(int j=i+1;j<n;j++){
                String str1 = words[i];
                String str2 = words[j];
                if(str1.length() > str2.length()) continue;
                if(str2.startsWith(str1) && str2.endsWith(str1)){
                    c++;
                }
            }
        }
        return c;
    }
}