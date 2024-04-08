#!/usr/bin/node
function add (a, b) {
  const args = process.argv;
  const numArgs = process.argv.length;
  let firstargument;
  let secondargument;
  if (numArgs < 3) {
    console.log(NaN);
  } else {
    firstargument = Number(args[2]);
    secondargument = Number(args[3]);
    console.log(firstargument + secondargument);
  }
}
add();
