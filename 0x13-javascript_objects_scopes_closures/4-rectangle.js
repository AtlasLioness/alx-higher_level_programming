#!/usr/bin/node
// class Rectangle that defines rectangle with 2 instance attributes width and height

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(parseInt(this.width)));
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width = parseInt(this.width) * 2;
    this.height = parseInt(this.height) * 2;
  }
};
