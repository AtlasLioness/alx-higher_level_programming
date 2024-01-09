#!/usr/bin/node
// function that returns the numbr of occurences in a list
exports.nbOccurences = function (list, searchElement) {
  let oc = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      oc += 1;
    }
  }
  return (oc);
};
