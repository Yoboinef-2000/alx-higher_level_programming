#!/usr/bin/node
const numargs = process.argv.length;
const allargs = process.argv;
if (numargs <= 3) {
  console.log(0);
} else {
  let highestnumber = Number(allargs[2]);
  let secondhighestnumber = Number.NEGATIVE_INFINITY;
  for (let i = 3; i < numargs; i++) {
    if (highestnumber < Number(allargs[i])) {
      secondhighestnumber = highestnumber;
      highestnumber = Number(allargs[i]);
    }
  }
  console.log(secondhighestnumber);
}
