// GOBACK BUTTON
// function goBack() {
//     window.history.back();
// }

//NAVIGATION
function openNav() {
  document.getElementById("sideNav").style.width= "100%";
}

function closeNav() {
  document.getElementById("sideNav").style.width = "0";
}
   
// SLIDE
var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("slides");
  if (n > slides.length) {slideIndex = 1}    
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none"; 
  }
  slides[slideIndex-1].style.display = "block";  
}

// Slider for Quotation
var slider = document.getElementById("font-weight-changer");

slider.addEventListener('input', function() {
    var size = slider.value;
    document.getElementById("font-change").style.fontWeight = size;
});