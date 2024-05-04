#!/usr/bin/node

const list = require('./100-data').list;
const New = list.map((v, i) => v * i);
console.log(list);
console.log(New);
