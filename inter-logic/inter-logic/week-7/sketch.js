let bubbles = [];
var score = 0;

function setup() {
  createCanvas(windowWidth, windowHeight);
  for (let i = 0; i < 160; i++) {
    let x = random(width);
    let y = random(height);
    let r = random(10, 20);
    let b = new Bubble(x, y, r);
    bubbles.push(b);
  }
}

function mousePressed() {
  for (let i = 0; i < bubbles.length; i++) {
    bubbles[i].clicked(mouseX, mouseY);
    console.log("Mouse has been pressed!");
  }
}

function draw() {
  background(50,80,100);
  
  if (score>19){
    scoreSuccess();
  }
  else{
    for (let i = 0; i < bubbles.length; i++) {
        let r = map(i,0,10,0,70);
        let g = map(i,0,60,50,120);
        let b = map(i,0,100,255,40);
        bubbles[i].move();
        bubbles[i].show(r,g,b);
        scoreNo();
    }
  }
}

class Bubble {
  constructor(x, y, r) {
    this.x = x;
    this.y = y;
    this.r = r;
    this.brightness = 200;
  }
  clicked(px, py) {
    let d = dist(px, py, this.x, this.y);
    if (d < this.r) {
      this.brightness = 0;
      score++;
    }
  }
  move() {
    this.x = this.x + random(-4, 4);
    this.y = this.y + random(-4, 4);

    if(this.x > windowWidth && this.y > windowHeight){
      this.x *= -2
      this.y *= -2
    }
    if(this.x < 0 && this.y < 0){
      this.x *= 2
      this.y *= 2
    }
  }
  show(rCol,gCol,bCol) {
    fill(rCol,gCol,bCol,this.brightness);
    noStroke();
    ellipse(this.x, this.y, this.r * 2);
  }
}

function scoreNo(){
  fill(0, 200, 250);
  textSize(24);
  text("Can you make it to 20?", 10, 30);
  text("Score: " + score, 10, 60);
}

function scoreSuccess(){
  fill(0, 200, 250);
  textSize(24);
  text("You did 20!",10,30);
}


