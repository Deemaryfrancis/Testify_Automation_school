//Calculate the sum of numbers within an array

let sumofNumber = [1, 2, 3, 15, 20, 34, 29, 67];
let sum = 0;
for(let i=0; i< sumofNumber.length; i++) {
    // sum = sum + scores[i];
    sum += sumofNumber[i]; 
}
console.log(sum);

function sumArry(arr) {
    let total = 0;

    for(i = 0; i < arr.length; i++ ) {
        total += arr[i];
    }
    return total;
}

console.log(sumArry([1,2,3,4,5,6]));
