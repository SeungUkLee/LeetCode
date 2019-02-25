/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let pos = 0;
    let len = nums.length;
    
    for (const num of nums) {
        if (num != 0) {
            nums[pos++] = num;
        }
    }
    
    while (pos < len) {
        nums[pos++] = 0;
    }
};