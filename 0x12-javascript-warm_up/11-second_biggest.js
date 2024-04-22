#!/usr/bin/node
// searches the second biggest int in the list of args

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const args = process.argv.slice(2).map(Number);
  const sorting = args.sort((a, b) => b - a);
  console.log(sorting[1]);
}
