/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    const res = parseInt(x.toString().split('').reverse().join(''))
    
    if ( x > 2147483647 || res> 2147483647 ) { 
        return 0; 
    } 
    
    return x > 0 ? res : -res 
};