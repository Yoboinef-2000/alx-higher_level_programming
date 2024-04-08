#!/usr/bin/node
function factorial (a) {
  if (a === 1 || a === 0) {
    return (1);
  } else {
    return (a * factorial(a - 1));
  }
}

const firstArgument = parseInt(process.argv[2]);
if (isNaN(firstArgument)) {
  console.log(1);
} else {
  console.log(factorial(firstArgument));
}
