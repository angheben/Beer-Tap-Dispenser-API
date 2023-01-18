var animationContainer = document.getElementById("animation-container");
var content = document.getElementById("content");
var audio = document.getElementById("video");

setTimeout(function() {
  audio.pause();
  animationContainer.style.display = "none";
  content.style.display = "block";
}, 5000);

audio.addEventListener("ended", function() {
  animationContainer.style.display = "none";
  content.style.display = "block";
});