/*
ANIMATED BALL
--------------
Circle to practice animation in p5.js
Exercise done after Dan Schiffman's classes on YouTube, videos from 7 to 9.
See https://www.youtube.com/playlist?list=PLRqwX-V7Uu6Zy51Q-x9tMWIv9cueOFTFA
*/

// Assign values to change later
let ball = {
  x: 0,				// x-axis position
  y: 0,				// y-axis position
  d: 30				// diameter
};

// Function setup() runs once
function setup() {
  createCanvas(600, 400);
}

// Function draw() runs in infinite loop
function draw() {
  background(250, 250, 100);

  fill(250, 200, 200);
  ellipse(ball.x, ball.y, ball.d, ball.d);
  ball.x += 1;
  ball.y += 1;
  ball.d += 0.5;
}