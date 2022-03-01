#!/usr/bin/node
const SquareParent = require('./5-square.js');
class Square extends SquareParent {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.height));
      }
    }
  }
}

module.exports = Square;
