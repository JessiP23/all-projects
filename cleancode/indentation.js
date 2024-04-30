//INDENTATION / NESTING


//example 1
/*
let  numbers = [1,2,3,4,5]
let sum = 0;
for(let i = 0; i < numbers.length; i++){
    sum += numbers[i];
}
console.log(sum);
*/

let numbers = [1,2,3,4,5];
let evenNumbers = [];

for(let i = 0; i < numbers.length; i++){
    if (numbers[i] % 2 === 0){
        evenNumbers.push(numbers[i]);
    }
}
let numbers1 = [1,2,3,4,5];
let evenNumbers1 = numbers1.filter(number => number % 2 === 0);




/*
function canViewContent(user){
    if(user){
        if(user.age){
            if(user.age >= 19){
                return true;
            }else{
                return false;
            }
        }else{
            return false;
        }
    }else{
        return false;
    }
}
*/
function canViewContent(user){
    if(!user || !user.age || user.age < 18){
        return false;
    }
    return true;
}


/*
function calculateDiscount(cart){
    let discount = 0;
    if(cart.total > 100){
        discount = cart.total * 0.1;
    }
    return discount;
}
*/

function calculateDiscount(cart){
    if(cart.total <= 100){
        return 0;
    }
    return cart.total * 0.1;
}








































