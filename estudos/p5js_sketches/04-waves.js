/*
WAVES
-----
Trying to recreate this gif (https://beesandbombs.tumblr.com/post/45513650541/orbiters)
*/

// Define time por future use
let t = 0;

function setup() {
  createCanvas(600, 400);
}

function draw() {
  background(255);
  
  // "add 25px to x while x <= width"
  for (let x = 0; x <= width; x += 25) {
    // "add 25px to y while y <= height"
    for (let y = 0; y <= height; y += 25) {
      // convert x value to get the angle, taking pi twice for each step from 0 to width value
      const xAngle = map(x, 0, width, 2 * PI, 2 * PI, true);
      // convert y value to get the angle, taking pi twice for each step from 0 to height value
      const yAngle = map(y, 0, height, 2 * PI, 2 * PI, true);
      const angle = xAngle * (x / width) + yAngle * (y / height);
      const myX = x + 25 * cos(2 * PI * t + angle);
      const myY = y + 25 * sin(2 * PI * t + angle);
      
      // Red dots
      noStroke();
      fill(139, 0, 0, 150);
      ellipse(myX, myY, 13);
      
      // Gray circle
      stroke(105, 105, 105, 150);
      noFill();
      ellipse(x, y, 50);
    }
  }
  // Increment time
  t += 0.015;
}
