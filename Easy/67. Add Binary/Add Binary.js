/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function(a, b) {
    let aLen = a.length - 1;
    let bLen = b.length - 1;
    let carry = 0;
    let res = '';
    
    while (aLen >= 0 || bLen >= 0 || carry == 1) {
        
        let aBit = aLen >= 0 ? parseInt(a[aLen--]) : 0;
        let bBit = bLen >= 0 ? parseInt(b[bLen--]) : 0;
        let sumBit = aBit + bBit + carry;
        
        sumBit >=2 ? carry = 1 : carry = 0;
        sumBit %= 2;
        res = `${sumBit}${res}`;    
    }
    return res;
};