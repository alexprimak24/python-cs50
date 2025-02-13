if (!localStorage.getItem("count")) {
  localStorage.setItem("count", 0);
}

function increment() {
  let count = localStorage.getItem("count");
  count++;
  document.querySelector("h1").innerHTML = count;
  localStorage.setItem("count", count);
}
// DOMContentLoaded wait for the whole content of the page to be loaded
// function () {} tells what content should be done when the done is done loading
document.addEventListener("DOMContentLoaded", function () {
  document.querySelector("h1").innerHTML = localStorage.getItem("count");
  document.querySelector("button").onclick = increment;

  // setInterval(increment, 1000);
});
