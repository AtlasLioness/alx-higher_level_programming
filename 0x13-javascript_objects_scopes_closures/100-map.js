#!/usr/bin/node
// script that imports an array and computes a new array

const data = require('./100-data.js').list;
console.log(data);
const mapping = data.map((element, index) => element * index);
console.log(mapping);
