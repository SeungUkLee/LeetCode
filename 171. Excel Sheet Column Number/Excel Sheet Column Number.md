# My Solution

~~~ js
/**
 * @param {string} s
 * @return {number}
 */

var titleToNumber = function(s) {
    const NUM = 26;
    const len = s.length;
    let res = 0;
    
    for (const [i,c] of s.split('').entries()) {
        res += Math.pow(NUM, (len - i - 1)) * (c.charCodeAt(0)-65+1) * '1';
    }
    
    return res;
};
~~~

# Best Pratice
~~~ js
var titleToNumber = function(s) { // Time: O(n), Space: O(1)
  var num = 0;
  for (var i = 0; i < s.length; i++) {
    num = num * 26 + (s.charCodeAt(i) - 'A'.charCodeAt(0) + 1);
  }
  return num;
};
~~~
