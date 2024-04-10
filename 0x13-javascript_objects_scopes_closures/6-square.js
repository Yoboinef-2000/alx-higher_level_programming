#!/usr/bin/node
const SquaresDaddy = require('./5-square');

class Square extends SquaresDaddy {
  charPrint (c) {
    let printCharacter = c;
    if (c === undefined) {
      printCharacter = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      for (let j = 1; j < this.width; j++) {
        process.stdout.write(printCharacter);
      }
      console.log(printCharacter);
    }
  }
}

module.exports = Square;
