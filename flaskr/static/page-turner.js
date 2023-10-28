function findClosestElement(elements) {
  let closestElement = null;
  let minDistance = Number.MAX_VALUE;

  elements.forEach(function(element) {
    const rect = element.getBoundingClientRect();
    const distance = Math.abs(rect.top);

    if (distance < minDistance) {
      minDistance = distance;
      closestElement = element;
    }
  });

  return closestElement;
}

let full_height = Math.max(
  document.body.scrollHeight, document.body.offsetHeight,
  document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight
);
let page_height = window.innerHeight;
let page_count = Math.floor(full_height / page_height);


// generates the page markers
for (let i = 0; i <= page_count; i++) {
  let page_marker = document.createElement("div");
  page_marker.setAttribute("id", "page-" + i);
  page_marker.setAttribute("class", "page");
  page_marker.style.position = "absolute";

  if (i == 0) {
    page_marker.style.top = "0px";
  } else {
    page_marker.style.top = (page_height * i) + "px";
  }
  page_marker.innerHTML = "&nbsp;";

  document.getElementById("main").appendChild(page_marker);
}


// handles the page turning
const pages = document.querySelectorAll(".page");
const targetElement = document.documentElement;

document.addEventListener('mousedown, touchend', function(event) {
  const clickX = event.clientX;
  const clickY = event.clientY;

  const targetRect = targetElement.getBoundingClientRect();


  if (
    clickX >= targetRect.left + ((targetRect.right / 3) * 2) &&
    clickX <= targetRect.right &&
    clickY >= targetRect.top &&
    clickY <= targetRect.bottom
  ) {
    let currentPage = findClosestElement(pages).id.substring(5);
    let nextPage = parseInt(currentPage) + 1
    nextPage = "#page-" + nextPage;

    // this means the page isn't going to be on the url
    document.querySelector(nextPage).scrollIntoView({
      behavior: 'smooth'
    });
  }
});
