/**
 * @param {number[]} nums
 * @return {number}
 */

/* Case 1 */
var maxSubArray = function(nums) {
    var curSum = totalSum = nums[0];
    for(var i=1; i<nums.length; i++) {
        curSum = Math.max(nums[i], curSum+nums[i])
        totalSum = Math.max(totalSum, curSum)
    }
    return totalSum;
};

/* Case 2 */
const maxSubArray = function(nums) {
    let curSum = 0;
    return nums.reduce((maxSum, curNum) => {
        curSum = Math.max(curSum + curNum, curNum);
        return Math.max(curSum, maxSum);
    }, nums[0])
};