var widthSplit 
var heightSplit

function setup() {
  createCanvas(windowWidth, windowHeight);
  noStroke();
}

function draw() {
  background(0);
  noFill()

  ellipse(mouseX, mouseY, 50, 50)
  stroke(255,255,255)
  rectMove()
}

function rectMove(){
  
  widthSplit = width / 2
  heightSplit = height / 2
  translate(widthSplit, heightSplit)
  for (var i = 0; i < 200; i++ ){ 
    angleMode(DEGREES);
    rectMode(CENTER);
    push()
    rotate(sin(frameCount + i*2)* 100)

    var r = map(sin(frameCount), -1, -1, 50, 255)
    // var g = map(cos(frameCount/2), -1, -1, 50, 255)
    // var b = map(sin(frameCount/4), -1, -1, 50, 255)
    stroke(r,255,255);

    rect (mouseX - widthSplit,mouseY - heightSplit,600 - i*3,600 - i*3,200-i);
    rect (mouseX - widthSplit,mouseY - heightSplit,600 + i*3,600 + i*3,200 +i);
    pop()
  }
}