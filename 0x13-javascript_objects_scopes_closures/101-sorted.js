#!/usr/bin/node
// script to import a dict of occurences by user id and compute dict of user ids by occurence

const data = require('./101-data.js').dict;
const newdata = {};
for (const key in data) {
  if (newdata[data[key]] === undefined) {
    newdata[data[key]] = [key];
  } else {
    newdata[data[key]].push(key);
  }
}
console.log(newdata);
