public class Solution {
    public String convert(String s, int numRows) {
        
        int len = s.length();
        int repeat = 2 * numRows - 2;
        String result = "";
        char[] ch = s.toCharArray();
        
        if(numRows == 1){
            return s;
        }else if (numRows == 2){
            for(int i = 0; i < len; i += 2){
                result += ch[i];
            }
            for(int i = 1; i < len; i += 2){
                result += ch[i];
            }
            return result;
        }
        
        for(int i = 0; i < numRows; i++){
            
            int j = i;
            if(i == 0 || i == (numRows - 1)){
                while(j < len){
                    result += ch[j];
                    j += repeat;
                }    
            }else{
                
                int cross = 2 * (numRows - i - 1);
                while(j < len){
                    result += ch[j];
                    if((j + cross) < len){
                        result += ch[j + cross];
                    }
                    j += repeat;
                }
            
            }
        
            
        }
        return result;
    }
}