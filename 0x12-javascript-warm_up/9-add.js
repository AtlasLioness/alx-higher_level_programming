#!/usr/bin/node
// adds to numbers, first arg and second arg

function add (a, b) {
  return (a + b);
}
console.log(add(parseInt(process.argv[2]), parseInt(process.argv[3])));
