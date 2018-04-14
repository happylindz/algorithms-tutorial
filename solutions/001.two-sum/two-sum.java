public class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        int len = nums.length;
        for(int i = 0; i < len; i++){
            
            for(int j = i + 1; j < len; j++){
                
                if(nums[i] + nums[j] == target){
                     int[] arr = {i, j};
                     return arr;
                }
                
            }
        }    
        int[] arr = {};
        return arr;
        
    }
}