#!/usr/bin/node
// prints x ti;s "C is fun" where X is first arg of script

const myString = 'C is fun';
let i = 0;

if (isNaN(process.argv[2]) === true) {
  console.log('Missing number of occurrences');
} else {
  while (i < parseInt(process.argv[2])) {
    console.log(myString);
    i++;
  }
}
