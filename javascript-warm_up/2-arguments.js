#!/usr/bin/node

import argv from 'node:process';

const argumentsLength = argv.length

if (argumentsLength === 1) {
    console.log('No argument');
} 
else if (argumentsLength === 2) {
    console.log('Argument found');
}
else {
    console.log('Arguments found');
}