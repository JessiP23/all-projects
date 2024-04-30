/*
function calculateTotal(cart){
    let total = 0;
    for(let i = 0; i < cart.length; i++){
        let item = cart[i];
        let price = item.price;
        if(item.isTaxable){
            price = price * 1.1;
        }
        if(item.discount){
            price = price - item.discount;
        }
        total += price;
    }
    return total;
}
*/

function calculateItemPriceWithTax(item){
    return item.isTaxable ? item.price * 1.10 : item.price;
}
function calculateItemPriceWithDiscount(item,price){
    return item.discount ? price - item.discount : price;
}
function calculateTotal(cart){
    let total = 0;
    for(let i = 0; i < cart.length; i++){
        let item = cart[i];
        let price = calculateItemPriceWithTax(item);
        price = calculateItemPriceWithDiscount(item,price);
        total += price;
    }
    return total;
}



/*
function registerStudent(student,className){
    if(class[className].students.length >= classes[className].maxSize){
        return "Class is full";
    }
    classes[className].students.push(student);
    let emailMessage = `Dear ${student.name}, you have been registered to ${className}.`;
    emailService.send(student.email, emailMessage);
    return "Registration succesfull";
}
*/

function isClassFull(className){
    return classes[className].students.length >= classes[className].maxSize;
}
function addToClass(student, className){
    classes[className].studnets.push(student);
}
function sendConfirmationEmail(student, className){
    let emailMessage = `Dear ${student.name}, you have been registered to ${className}.`;
    emailService.send(student.email, emailMessage);
}
function registerStudent(student,className){
    if(isClassFull(className)){
        return "Class is full";
    }
    addToClass(student, className);
    sendConfirmationEmail(student,className);

    return "Registration succesfull";
}



