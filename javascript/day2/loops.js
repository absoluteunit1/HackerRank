// My solution 

function vowelsAndConsonants(s) {
    var vowels = ['a', 'e', 'i', 'o', 'u'];
    for(let letter of s){
        for(let vowel of vowels){
            if(letter === vowel){
                console.log(letter);
            }
        }
    }
    for(let letter of s){
        if(!vowels.includes(letter)){
            console.log(letter)
        }
        
    }
}
