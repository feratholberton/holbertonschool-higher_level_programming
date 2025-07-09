#!/usr/bin/node

const { argv } = require('node:process');

const repeatTimes = parseInt(argv[2]);
const phrase = 'C is fun';

if (isNaN(repeatTimes)) {
  console.log('Missing number of occurrences');
} else {
  let count = 0;
  while (count < repeatTimes) {
    console.log(phrase);
    count++;
  }
}
