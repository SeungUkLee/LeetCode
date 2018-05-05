/**
 * @param {string} S
 * @return {string}
 */
var toGoatLatin = function(S) {
    const vowel = ['a','e','i','o','u', 'A','E','I','O','U'];
    const vowelSet = new Set(vowel);
    
    return S.split(' ').map((word, i) => {
        return vowelSet.has(word[0]) ? word+'ma'+'a'.repeat(i+1) : word.slice(1)+word.slice(0,1)+'ma'+'a'.repeat(i+1);        
    }).join(' ');
    
};
