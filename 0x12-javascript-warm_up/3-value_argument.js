#!/usr/bin/env node
const args = process.argv;
if (args[0] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
