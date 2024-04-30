//let radius1 = 5;
//let area1 = Math.PI * radius1 * radius1

//let radius2 = 5;
//let area2 = Math.PI * radius2 * radius2


// ------------------------------
//correct version
function calculateArea(radius){
    return Math.PI * radius * radius
}
let radius1 = 5;
let area1 = calculateArea(radius1)

let radius2 = 5;
let area2 = calculateArea(radius2)



//EXAMPLE 2
document.getElementById("element1").innerText = "Hello, world";
document.getElementById("element2").innerText = "Hello, world";
document.getElementById("element3").innerText = "Hello, world";

// ----------------------------------
function setText(elementId, text){
    document.getElementById(elementId).innerText = text;
}
setText('element1','Hello, World!');
setText('element2','Hello, World!');
setText('element3','Hello, World!');


//Example 3
/* 
let array1 = [1,2,3];
let sum1 = 0;
for(let i = 0; i < array1.length; i++){
    sum1 += array1[i]
}
let array2 = [4,5,6];
let sum2 = 0;
for(let i = 0; i < array2.length; i++){
    sum2 += array2[i]
}
*/
// -----------------------------------
function calculateSum(array){
    let sum = 0;
    for(let i = 0; i < array.length; i++){
        sum += array[i]
    }
    return sum;
}
let array1 = [1,2,3];
let sum1 = calculateSum(array1);
let array2 = [4,5,6];
let sum2 = calculateSum(array2);

