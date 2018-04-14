/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int low = 1, high = n;
        while(low <= high){
            
            int middle = low + (high - low) / 2;

            if(isBadVersion(middle) && !isBadVersion(middle - 1)){
                return middle;
            }
            
            if(isBadVersion(middle)){
                high = middle - 1;
            }else{
                low = middle + 1;
            }
        }
        return -1;
    }
}