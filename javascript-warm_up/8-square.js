#!/usr/bin/node

const { argv } = require('node:process');

const size = parseInt(argv[2]);
const character = 'X';

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let row = "";
    for (let j = 0; j < size; j++) {
      row += character;
    }
    console.log(row);
  }
}
