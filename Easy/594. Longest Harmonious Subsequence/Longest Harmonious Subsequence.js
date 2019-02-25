/**
 * @param {number[]} nums
 * @return {number}
 */

 var findLHS = function(nums) {
    const map = {};
    let max = 0;
    nums.forEach((one,index) => {
        if(map[one]!=undefined){
            map[one]++;
        } else {
            map[one] = 1;
        }
        if(map[one]+map[one+1]>max){
            max = map[one] + map[one+1]
        }
        if(map[one]+map[one-1]>max){
            max = map[one] + map[one-1]
        }
    })
    return max;
};