#!/usr/bin/node
// script that prints a msg depening on no of args passed

const argc = process.argv.length - 2;

if (argc === 0) {
  console.log('No argument');
} else if (argc === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
