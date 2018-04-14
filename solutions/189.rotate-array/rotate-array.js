/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    
    for(var i = 0; i < k; i++){
        
        var removed = nums.pop();
        
        nums.unshift(removed);
    }
    
};