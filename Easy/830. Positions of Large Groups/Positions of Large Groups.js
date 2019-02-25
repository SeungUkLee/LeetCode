/* Use Two Pointer */

/**
 * @param {string} S
 * @return {number[][]}
 */
var largeGroupPositions = function(S) {
    let res = [];
    let start = 0;
 
    for (let i=0; i<S.length; i++) {
        if (S[i+1] !== S[i] || i === S.length - 1) {
            if (i-start + 1 >= 3) {
                res.push([start, i]);
            }
            start = i+1
        }    
    }   
    
    return res;
};