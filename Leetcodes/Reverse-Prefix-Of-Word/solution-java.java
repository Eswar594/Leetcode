class Solution {
    public String reversePrefix(String word, char ch) {
        int a = word.indexOf(ch);
        if (a != -1) {
            StringBuilder pref = new StringBuilder(word.substring(0, a + 1));
            String revpref = pref.reverse().toString();
            return revpref + word.substring(a + 1);
        }
        return word;
    }
}