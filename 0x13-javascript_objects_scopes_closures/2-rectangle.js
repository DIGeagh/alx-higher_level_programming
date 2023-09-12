#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0) {
      // If w or h is <= 0, create an empty object
      return {};
    }

    // Initialize instance attributes width and height
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
