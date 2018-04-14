public class Solution {
    public int reverse(int x) {
        if(x == -2147483648){
            return 0;
        }
        boolean isNegative = false;
        String result = "";

        if (x >= 0) {
        } else {
            isNegative = true;
        }

        x = Math.abs(x);


        while (x != 0) {

            int val = x % 10;
            result += val;
            x /= 10;

        }

        if(result == ""){
            return 0;
        }
        Double num = Double.parseDouble(result);
        if(num >= 2147483648.0){
            return 0;
        }

        if (isNegative == true){
            return -Integer.parseInt(result);
        }

        return Integer.parseInt(result);

    }
}