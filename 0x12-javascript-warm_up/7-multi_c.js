#!/usr/bin/node
// prints x times "C is fun" where x is the first arg of script

const string = 'C is fun';
const arg = process.argv[2];
const converted = parseInt(arg);

if (!isNaN(converted)) {
  for (let i = 0; i < converted; i++) {
    console.log(string);
  }
} else {
  console.log('Missing number of occurrences');
}
