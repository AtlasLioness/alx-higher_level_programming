#!/usr/bin/node
// script that concats 2 files

const fs = require('fs');
const first = fs.readFileSync(process.argv[2]).toString();
const second = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], first + second);
