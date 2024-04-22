#!/usr/bin/node
// computes and prints a factorial

// function definition
function factorial (a) {
  if (isNaN(a)) {
    return 1;
  } else if (a < 0) {
    return NaN;
  } else if (a === 0) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}

const arg = parseInt(process.argv[2]);
const fact = factorial(arg);

console.log(fact);
