/*
LOGO
----
Static shapes to form my logo and get to learn a bit of p5.js
Exercise done after Dan Schiffman's classes on YouTube, videos from 1 to 6.
See https://www.youtube.com/playlist?list=PLRqwX-V7Uu6Zy51Q-x9tMWIv9cueOFTFA
*/

function setup() {              // set up the container to present graphic items
  createCanvas(400, 400);       // size (400px for width; 400px for height)
}

function draw() {               // Present graphic items 
  background(100, 110, 120);    // RGB-format color of canvas background
  
  // Settings
  stroke(255);                  // color of stroke (white)
  strokeCap(SQUARE);           	// line endings of stroke (not rounded)
  strokeWeight(20);             // weight of stroke (20px)
  noFill();                     // transparent
  
  // Shapes
  rect(110, 110, 80, 180, 0, 90, 0, 0);
  circle(250, 150, 80);
}

/*
SYNTAX
------

createCanvas(w, h, [renderer])
- w, h: width, height
- renderer [optional]: P2D (for 2D graph) or WEBGL (for 3D graph); default: P2D
ref: http://p5js.org/reference/#/p5/createCanvas

background(c, [a])
- c: grayscale (single value), RGB (three values), hex (single value as string), or image
- a [optional]: alpha (or opacity)
ref: http://p5js.org/reference/#/p5/background

stroke(c, [a])
- c: grayscale (single value), RGB (three values), or hex (single value as string)
- a [optional]: alpha (or opacity)
ref: http://p5js.org/reference/#/p5/stroke

strokeCap(cap)
- cap: either SQUARE, PROJECT, or ROUND; default: ROUND
ref: http://p5js.org/reference/#/p5/strokeCap

strokeWeight(weight)
- weight: number in pixels of weight
* half of weight is inside the element, half is outside
ref: http://p5js.org/reference/#/p5/strokeWeight

noFill()
ref: http://p5js.org/reference/#/p5/noFill

rect(x, y, w, h, [tl], [tr], [br], [bl])
- x, y: the pair of values representing the pixel where the rect starts
- w, h: width, height
- tl, tr, br, bl: radius for top-left, top-right, bottom-right, bottom-left corners
* if only one value is given it is the radius for all corners
ref: http://p5js.org/reference/#/p5/rect

circle(x, y, d)
- x, y: the pair of values representing the pixel which is the center of the circle
- d: diameter
ref: http://p5js.org/reference/#/p5/circle
*/