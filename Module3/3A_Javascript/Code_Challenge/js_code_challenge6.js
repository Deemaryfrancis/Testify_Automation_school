//Sort an array of strings in alphabetical order

const nameOfFruits = ['Apple','Orange','Banana','Pawpaw', 'Mango', 'Watermelon']
nameOfFruits.sort();
console.log(nameOfFruits);

console.log('=== or ===');

nameOfFruits.sort(function(a, b){return a-b});
console.log(nameOfFruits);

