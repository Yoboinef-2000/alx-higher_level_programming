#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (((w = parseInt(w)) > 0) && ((h = parseInt(h)) > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      for (let j = 1; j < this.width; j++) {
        process.stdout.write('X');
      }
      console.log('X');
    }
  }
}
module.exports = Rectangle;
