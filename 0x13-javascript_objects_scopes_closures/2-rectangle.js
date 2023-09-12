#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0) {
      // Create an empty object if w or h is <= 0
      return {};
    } else {
      // Initialize instance attributes width and height
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
