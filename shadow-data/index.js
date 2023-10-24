// // NAVIGATION
function openNav() {
  document.getElementById("sideNav").style.width= "100%";
}
  
function closeNav() {
  document.getElementById("sideNav").style.width = "0";
}

//P5.JS
var sketchWidth;
var sketchHeight;
function setup() {
  background(200, 200, 200);
  sketchWidth = document.getElementById("canvas").offsetWidth;
  sketchHeight = document.getElementById("canvas").offsetHeight;
  
  let renderer = createCanvas(sketchWidth, sketchHeight);
  renderer.parent("canvas");
}

function draw() { 
  if (mouseIsPressed){
    mouseBrush();
  }
} 

function mouseBrush(){
  let mousetext = mouseX + '.' + mouseY;
  const w = color(255, 255, 255);
  const b = color(0,0,0)
  fill(w);
  stroke(b);
  strokeWeight(2);  
  textSize(30);
  text(mousetext, mouseX, mouseY); 
}

function clearArt(){
  clear(); 
}

function saveArt(){
  save('art.jpg');
}