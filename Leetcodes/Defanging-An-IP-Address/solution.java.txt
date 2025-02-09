1. Method-1:
class Solution {
    public String defangIPaddr(String address) {
        String s = "";
        for(int i = 0; i < address.length(); i++){
            if (address.charAt(i) == '.'){
                s += "[.]";
            }
            else{
                s += address.charAt(i);
            }
        } 
        return s;
    }
}

2.Method-2:

class Solution {
    public String defangIPaddr(String address) {
        StringBuffer sb=new StringBuffer(address);
        String result=sb.toString().replace(".","[.]");
        return result;
    }
}