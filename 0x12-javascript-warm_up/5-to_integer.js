#!/usr/bin/node
// prints My number: <first argument converted in integer> if the first argument can be converted to an integer

const arg = process.argv[2];
const intConv = parseInt(arg);

if (!isNaN(intConv)) {
  console.log('My number: ' + intConv);
} else {
  console.log('Not a number');
}
