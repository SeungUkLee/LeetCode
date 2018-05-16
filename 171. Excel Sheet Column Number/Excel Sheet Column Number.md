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

