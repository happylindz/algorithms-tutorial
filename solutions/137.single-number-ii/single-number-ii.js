/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    
    var numsSet = {};
    
    for(var i = 0, len = nums.length; i < len; i++){
        
        if(numsSet[nums[i]] === undefined){
            numsSet[nums[i]] = 1;
        }else{
            numsSet[nums[i]] ++;
        }
        
    }
    
    for(var num in numsSet){
        if(numsSet[num] == 1){
            return +num;
        }
        
    }
    
        return -1;

};