#!/usr/bin/node
// script that prints a square with size of first arg

const arg = process.argv[2];
const integer = parseInt(arg);

if (!isNaN(integer)) {
  for (let i = 0; i < integer; i++) {
    console.log('X'.repeat(integer));
  }
} else {
  console.log('Missing size');
}
