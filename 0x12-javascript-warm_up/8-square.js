#!/usr/bin/env node
const numArgs = process.argv.length;
if (numArgs < 2) {
  console.log('Missing size');
} else {
  const firstArgument = parseInt(process.argv[2]);
  if (isNaN(firstArgument)) {
    console.log('Missing size');
  } else {
    for (let i = 0; i < firstArgument; i++) {
      for (let j = 1; j < firstArgument; j++) {
        process.stdout.write('X');
      }
      console.log('X');
    }
  }
}
