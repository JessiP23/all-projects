#Big O Notation 
'''
is used to classify algorithms according to how their run tie or space requirements grow as the input size grows

Theory
f(n)=O(g(n)) (f is Big-O of g) of f<=g if there exists constants
N and c so that for all n>=N, f(n)<=c*g(n)

Example:
total=0
for i in n:
    total += i
    print(i)

    n refers to the size of our input    
    2n + 1 is the number of operations
    1 operation to define the variable
    n loops and 2 operations inside the loop

    To find g(n) and N, we gotta exclude constant in f(n)

2n+1 <= c*g(n) 
n = c*g(n)
this tells us g(n) which is n.  g(n) = n
n = c * n
lets find a constant c such as accomplishes the function above 2n+1<=c*g(n)
lets make c=3 and its true. our big o notation is O(n)


Quiz Examples
What do we mean when we say that an algorithm A has a faster runtime than B?
Reason: A will tipically perform better on larger inputs
Explanation: In Big O Notation, we consider the growth of the algorithms in terms of input size. 



Order of time complexities from fastes to lowest?
0(1) < 0(log n) < O(n) < O(n^2)
Explanation: O(1) represents a constant time complexity, which is the fastest. O(log n) which is faster than linear but slower than constant. 
O(n) is linear time complexity, slower than algorithmic but faster than quadratic. And O(n^2) is the slowest.



What would be the runtime of the function. The following code shows a function that calculates the remainder of a division operation?
CODE:
function mod(a,b){
    if(b <= a) return -1;
    const div = Math.floor(a / b);
    return a - div * b;
}
Reason: O(1)
Explanation: This code consists of a few simple arithmetic operations: division, multiplication, and subtraction. These operations have constant time complexity, 
meaning the execution time does not depend on the size of the input. Therefore, the runtime is considered constant, or O(1)



The following code shows a function that checks if a given number is prime. What would be the runtime of the function?
CODE: 
function isPrime(n){
if(n < 2 || n % 1!= 0){
    return false;
}
    for(let i = 2; i < n; i++){
        if(n % 1 == 0) return false;
    }
    return true;
}
Reason: O(n)
Explanation: The for loop is the block that determines the time complexity, as it iterates through each item one time. Therefore the time complexity of the code is O(n)



This function returns the number of elements that exist inside both input arrays. What is the runtime of the function? 
Hint. The sorting and searching functions have a runtime of O(n log n) and O(log n).
CODE:
function countIntersect(a,b){
    let count = 0
    a.sort()

    for(let i = 0; i < a.length; i++){
        if(search(b, a[i])){
            count++
        }
    }
    return count
}
Reason: O(a log a + a log b)
Explanation: The sort operation has an average runtime of O(a log a), where a is the length of the list input array.
The search operation has an average runtime of O(log b), where b is the length of the second input array
The for loop has a runtime of O(a) since it iterates over the first input array
The overall runtime is O(a log a + a log b)
'''



'''
Analyzing Algorithms (Practice & Examples)
function example1(num){
    return num % 2 == 0;
} 
Result: O(1)
time complexity is gonna be based on the size of the input


function example2(nums):
    let total = 0;  1 operation
    for(const number of nums){
        total += nums                        n operations
    }
Once we have a for means we have to loop N times. Not always but the majority of it
Answer: O(n)



function example3(nums){
    const results = Array(nums.length).fill(1);    n operations because for everys single value we gotta make a single value 
    for(let [i,num1] of nums.entries()){           n operations  |
        for(const num2 of nums){                |                |  2n^2 operations
            if(num1 === num2) continue;         | 2n operations  |
            results[i] *= num2;                 |                |
        }
    }
}
return results;                                  1 opertion
 number of operations 2n^2 + n + 1
 Big O Function  O(n^2)

take an array and produce another array with 1's




function example4(nums1,nums2){
    const results = []             1 operation
    for(const num of nums1){       n times
        results.push(num);
    }
    for(let[i,num] of nums2.entries()){      m times|
        if(i >= results.length){             1      |
            results.push(1)                  1      |    3m operations
        }                                           |
        results[i] *= num;                    1     |
    }
    return results;
}

2 + n + 3m           BOF     O(n + m)


when having two parameters, we denote with different letters the number of operations of each parameter
n is the size of num1 and m is the size of num2



function example5(nestedArr){              
    let total = 0;                               1
    for(const innerArr of nestedArr){            H
        for(const num of innerArr){              W
            total += num;
        }
        for(const num of innerArr){                  W
            total += num;
        }
        for(const num of innerArr){                  W
        total += num;
        }
    }
    return total;                                 1
}

BOF    O(h*w)

h is the number of arrays that exists inside of the array
w is the width of the array



This is called recursion
This example is the Fibonacci sequence
function example6(n){
    if(n===1) return 1;
    if(n===2) return 1;
    const last = example6(n-1);
    const secondLast = example6(n-2);
    return last + seconLast;
}
the number of operations is O(2^n)
recursive cases are cases that repeat with the same function


function example7(arr, searchList){
    let max = Math.max(...arr);               n times
        for(const value of searchList){       m times  
        if(max === value) return true;
    }
    return false;
} 
O(n+m)


function example8(n){
    if(n===0) return;
    console.log(n);
    example8(Math.floor(n/2));
}
O(log2(n))
if the number were divided  by 3 then we'd have log3(n)

ALWAYS LOOK AT THE WORST POSSIBLE CASE
function getDigits(){
    const digist = [];
    for(let i = 0; i < 10; i++){        1
        digits.push(i);
    }
    return digits;
}                                                      n is the length of the structure
function example9(strings){                            K is the max length that exist in our strings
    for(const [i,string] in strings.entries()){       n operations
        let digits=0;
    }
    for(const char of string){                        k times
        if(getDigits().includes(char)) digits += 1;   1 time   because getDigits is constant 
    }
    if (digits >= string.length / 2){                 klog2(k)  operations       
        strings[i] = string.split("").sort().join("")     split takes k times, sort takes klog2(k), join takes k operations. In total gives us 2k+klog2(k)
    }
}
O(n(k+klog2(k))) = O(n * klog2(k))


function example11(nums){
    const sumToEnd = [];
    let count = 0;
    for(let i = 0; i < nums.length; i++){         n
        sumToEnd.push(0);
        for(let j=i+1; j<nums.length; j++){       n
            const num2 = nums[j];
            sumtoEnd[i] += num2;
            for(const x of sumToEnd){             n
                count+= 1;
                console.log(count);
            }
        }
    }
}
O(n^3)




function example12(n){
    if(n === 1) return 1;
    let total = 0;
    for(let x = 0; x < n; x++){
        total += example12(n-1);
    }
    return total;
}
O(n!)
'''

'''
QUIZ QUESTIONS 
The following code shows a function that returns the sum of two numbers. What is the time complexity of the algorithm?
CODE:
function sum(a,b){
    return a + b;
}
Reason: O(1)
Explanation: The fucntion performs a simple addition opearion and returns the result which does not depend on the size of the input. The time complexity is a constant


The following code shows a function that identifies whether a given string contains only unique characters. What is the time complexity of the function?
CODE:
function hasUniqueCharacters(str){
    const chars = new Set();
    for(const char of str){
        if(chars.has(char)){
            return false;
        }
        chars.add(char);
    }
    return true;
}
Reason: O(n)
Explanation: The dominant factor in terms of time complexity is the iteration over the characters in the string, which has a linear complexity of O(n).
Other operations, like adding or checking for elements in the set, have constant time complexities.


The followind code checks if a number is a power of two. What is the time complexity of the function?
CODE:
function isPowerOfTwo(n){
    if(n <= 0){
        return false;
    }
    while (n > 1){
        if(n % 2 !== 0){
            return false;
        }
        n = n/2;
    }
    return true;
}
Reason: O(log n)
Explanation: Since the number is halved in each iteration, the number of iterations needed to reach the result grows logarithmically as the input size increases. Therefore the time complexity of the function is lograithmic, O(logn)



The following code shows a function that counts the number of vowels in a given string. What is the time complexity of the function?
CODE:
function countVowels(str){
    const vowels = ['a','e','i','o','u'];
    let count = 0;
    for(let i = 0; i < str.length; i++){
        if(vowels.includes(str[i].toLowerCase())){
            count++;
        }
    }
    return count;
}
Reason: O(n)
Explanation: The operation of checking if a characer is a vowel by using includes takes constant time O(1), since the vowels array has a constant number of elements. However, since we perform this operation for each character in the string, the overall time complexity is determined by the number of characters in the input string, which results in O(n) complexity.



The following code shows a function findMax that takes an array as input and finds the maximum element in the arra. What is the time complexity of the function?
CODE:
function findMax(arr){
    let max = arr[0];
    for(let i = 0; i < arr.length; i++){
        if(arr[i] > max){
            mar = arr[i];
        }
    }
    return max;
}
Reason: O(n)
Explanation: The function findMax has a runtime of O(n), where n is the number of elements in the input array. It iterates through each element of the array once, comparing it with the current maximum value. The time compelxity of the function is therefore linear in respect to the size of the input. 


The following code computes the greates common divisor of two numbers. What is its time complexity?
CODE:
function gcd(a,b){
    if(b<a){
    [a,b] = [b,a];
    }
    while (b > 0){
        let r = a % b;
        a = b;
        b = r;
    }
    return a;
}
Reason: O(log n)
Explanation: The greatest common divisor of Euclidean algorithm has a time complexity of O(log n). This is because in each iteration of the while loop, the value of b is reduced by at least half. Therefore, the number of iterations needes is proportional to log n.


The following function hcecks ig an array contain duplicate elements. What is the time complexity of the function?
CODE:
function containsDuplicate(strings){
    for(let i = 0; i < strings.length; i++){
        for(let j = i+1; j < strings.length; j++){
            if(strings[i] === strings[j]){
                return true;
            }
        }
    }
    return false;
}
Reason: O(n^2)
Explanation: The containsDuplication function uses two nested loops to compare each string in the array with every other string in the array. These loops both
iterate approximately n times (the number of elements in the input array), so teh time complexity of the function is O(n^2).



The following code demonstrates a countdown process that divides the current value by 2 until it reaches 0. What is the time complexity of this algorithm?
CODE:
function halvingCountdown(n){
    let x = n;
    while (x > 0){
        let y = x;
        while (y > 0){
            y = Math.floor(y/2);
        }
        x = x-1;
    }
}
Reason: O(n log n)
Explanation: The outer loop iterates n times. The number of times the inner loop iterates is equal to the number of times we can halve n before we reach 1. This is equal to log n. Therefore, the time complexity of this algorithm is O(n log n)


The Tower of Hanoi is a mathematical puzzle that involves moving a stack of disks from one tower to another. You can only move one disk at a time and you can only place a smaller disk on top of a larger disk. 
The following code insists of a recursive function that describes this puzzle. What is the time complexity of the function?
CODE:
function towerOfHanoi(n,source,auxiliary,destination){
    if(n===1){
        console.log(`Move disk 1 from ${source} to ${destination}`);
        return;
    }
    towerOfHanoi(n-1,source,destination,auxiliary);
    console.log(`Move disk ${n} from ${source} to ${destination}`);
    towerOfHanoi(n-1, auxiliary, source, destination);
}
Reason: O(2^n)
Explanation: The Tower of Hanoi puzzle is a classic example of a recursive algorithm. The number of operations required to solve the problem frows exponentially with the number of disks, so the time complexity is O(2^n)


The following code is an implementation of the bubble sort algorithm. What is the time complexity of the algorithm?
CODE:
function bubblesort(arr){
    const n = arr.length;
    for(let i = 0; i < n; i++){
        for(let j = 0; j < n-i-1; j++){
            if(arr[j] > arr[j + 1]){
                let temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
    return arr;
}
Reason: O(n^2)
Explanation: The bubble sort algorithm has a runtime of O(n^2), where n is the number of elements in the input array. The algorithm of two nexted loops, each of which iterates over the array.
'''














































































































































































































































