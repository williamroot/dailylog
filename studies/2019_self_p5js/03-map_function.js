/*
MAP FUNCTION
------------
Exercising map function to change bg color according to mouse position
Exercise done after Dan Schiffman's classes on YouTube.
See https://www.youtube.com/playlist?list=PLRqwX-V7Uu6Zy51Q-x9tMWIv9cueOFTFA
*/

// Variable to place RGB values
let color = {
  r: 0,
  g: 0,
  b: 0
};

function setup() {
  createCanvas(600, 400);
}

function draw() {
  color.r = map(mouseX, 0, 600, 0, 255);  // mouseX: mouse position on x-axis
  color.g = map(mouseY, 0, 400, 0, 255);  // mouseY: mouse position on y-axis
  background(color.r, color.g, color.b);
  noFill();
  stroke(255);
  strokeWeight(5);
  ellipse(mouseX, mouseY, 30, 30);
}

/*
SYNTAX
------

map(value, start1, stop1, start2, stop2, [withinBounds])
- value: number or variable with number representing the incoming value to be converted
- start1: lower bound of the value's current range
- stop1: upper bound of the value's current range
- start2: lower bound of the value's target range
- stop2: upper bound of the value's target range
- withinBounds [optional]: boolean to constrain the value to the newly mapped range
ref: https://p5js.org/reference/#/p5/map
*/
