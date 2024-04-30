/*
let d = new Date();
let y = d.getFullYear();
let m = d.getMonth();
*/

let currentDate = newDate();
let currentYear = currentDate.getFullYear();
let currentMonth = currentDate.getMonth();

//Example 2
/*
function x(y,z){
    return y * y + z * z;
}
*/
function sumOfSquares(number1, number2){
    return number1 * number1 + number2 * number2
}

//Example 3
/*
class A{
    constructor(b,c){
        this.b = b;
        this.c = c;
    }
}
*/
class Car{
    constructor(make, model){
        this.make = make;
        this.model = model;
    }
}


//Example 4
/*
let p = 3.14;
let x = 5;
let y = 10;
function f(a,b){
    return p * a * a * b;
}
let z = f(x,y);
console.log(z);
*/

const PI = 3.14;
let radius = 5;
let height = 10;
function calculateCylinderVolume(radius,height){
    return PI * radius * radius * height;
}
let cylinderVolume = calculateCylinderVolume(radius, height);
console.log(cylinderVolume);









