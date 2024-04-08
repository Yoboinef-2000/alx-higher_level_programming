#!/usr/bin/node
const args = process.argv;
const numArgs = process.argv.length;
let firstargument;
let secondargument;
if (numArgs < 2) {
  firstargument = 'undefined';
  secondargument = 'undefined';
} else if (numArgs === 3) {
  firstargument = args[2];
  secondargument = 'undefined';
} else {
  firstargument = args[2];
  secondargument = args[3];
}
console.log(firstargument + ' is ' + secondargument);
