#!/usr/bin/node
// prints the adition of 2 integer using funtion add(a, b)

// function definition
function add (a, b) {
  return a + b;
}

const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);

console.log(add(arg1, arg2));
