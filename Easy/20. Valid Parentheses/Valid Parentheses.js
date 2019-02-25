/**
 * @param {string} s
 * @return {boolean}
 */

const map = {
    "(" : ")",
    "{" : "}",
    "[" : "]",
}

var isValid = function(s) {
    const stk = [];
    
    for (const k of s) {
        if (map[k]) {
            stk.push(map[k])
        } else {
            if (stk.pop() !== k) {
                return false;
            }
        }
    }

    return stk.length === 0;
};