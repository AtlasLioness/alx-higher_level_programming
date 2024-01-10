#!/usr/bin/node
// prints number of args already printed and the nez arg value
let count = 0;
exports.logMe = function (item) {
  console.log(`${count++}: ${item}`);
};
