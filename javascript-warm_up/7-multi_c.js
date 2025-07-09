#!/usr/bin/node

const { argv } = require('node:process');

const repeat_times = parseInt(argv[2]);
const phrase = 'C is fun';

if (isNaN(repeat_times)) {
    console.log('Missing number of occurrences');
} else {
  let count = 0;
  while (count < repeat_times) {
    console.log(phrase);
    count++;
  }
}
