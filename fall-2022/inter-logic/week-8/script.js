// https://kylemcdonald.github.io/cv-examples/
// https://github.com/kylemcdonald/AppropriatingNewTechnologies/wiki/Week-2

var capture;
var tracker
var w = 640,
    h = 480;
var leftEye;
var rightEye;
var toaster;

function preload(){
  leftEye = loadImage("left.png")
  rightEye = loadImage("right.png")
  toaster = loadImage("toaster.png")
}

function setup() {
    capture = createCapture({
        audio: false,
        video: {
            width: w,
            height: h
        }
    }, function() {
        console.log('capture ready.')
    });
    capture.elt.setAttribute('playsinline', '');
    createCanvas(w, h);
    capture.size(w, h);
    capture.hide();

    // colorMode(HSB);

    tracker = new clm.tracker();
    tracker.init();
    tracker.start(capture.elt);
}

function draw() {
    image(capture, 0, 0, w, h);
    var positions = tracker.getCurrentPosition();

    noFill();
    stroke(187,156,241);
    beginShape();
    for (var i = 0; i < positions.length; i++) {
        vertex(positions[i][0], positions[i][1]);
    }
    endShape();

    noStroke();
    for (var i = 0; i < positions.length; i++) {
        fill(241,156,187);
        ellipse(positions[i][0], positions[i][1], 4, 4);
        fill(255,255,153);
        // textSize(20);
        // text(i, positions[i][0], positions[i][1]);
    }
  
    if (positions.length > 0) {
        //eye
        image(leftEye,positions[63][0]-20,positions[64][1],60,40)
        image(rightEye,positions[68][0],positions[67][1],60,40)
      
        image(toaster,positions[61][0],positions[44][1],80,50)
      
        fill(255,255,4);
        ellipse(positions[2][0], positions[2][1], 4, 4);
      
        fill(255);
        textSize(20);
        text("I'm late!", positions[1][0]-100, positions[1][1]);
        // uncomment for a surprise
        // noStroke();
        // fill(0, 255, 255);
        // ellipse(positions[62][0], positions[62][1], 50, 50);
    }
}
