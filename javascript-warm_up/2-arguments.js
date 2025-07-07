#!/usr/bin/node

// import argv from 'node:process';
const { argv } = require('node:process');

const argumentsLength = argv.length;

// console.log(argumentsLength);

if (argumentsLength === 2) {
    console.log('No argument');
} 
else if (argumentsLength === 3) {
    console.log('Argument found');
}
else {
    console.log('Arguments found');
}