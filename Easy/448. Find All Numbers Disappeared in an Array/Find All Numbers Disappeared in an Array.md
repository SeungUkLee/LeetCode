## My Solution 

~~~ js
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDisappearedNumbers = function(nums) {
    const array = Array.from({length: nums.length}, (v, k) => k+1); 
    
    return array.filter(el => nums.indexOf(el) === -1);
};
~~~


## Another Solutions
The basic idea is that we iterate through the input array and mark elements as negative using `nums[nums[i] -1] = -nums[nums[i]-1].` In this way all the numbers that we have seen will be marked as negative. In the second iteration, if a value is not marked as negative, it implies we have never seen that index before, so just add it to the return list.

~~~ java
public List<Integer> findDisappearedNumbers(int[] nums) {
    List<Integer> ret = new ArrayList<Integer>();
    
    for(int i = 0; i < nums.length; i++) {
        int val = Math.abs(nums[i]) - 1;
        if(nums[val] > 0) {
            nums[val] = -nums[val];
        }
    }
    
    for(int i = 0; i < nums.length; i++) {
        if(nums[i] > 0) {
            ret.add(i+1);
        }
    }
    return ret;
}
~~~

~~~ java
public List<Integer> findDisappearedNumbers(int[] nums) {
    List<Integer> res = new ArrayList<>();
    int n = nums.length;
    for (int i = 0; i < nums.length; i ++) nums[(nums[i]-1) % n] += n;
    for (int i = 0; i < nums.length; i ++) if (nums[i] <= n) res.add(i+1);
    return res;
}
~~~