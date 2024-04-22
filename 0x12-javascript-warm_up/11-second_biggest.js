#!/usr/bin/node
// searches the second biggest int in the list of args

if (process.argv.length < 3) {
  console.log('0');
} else if (process.argv.length === 3) {
  console.log('0');
} else {
  const sorting = process.argv.sort();
  console.log(sorting.reverse()[1]);
}
