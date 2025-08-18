// List of breaking news headlines
const headlines = [
  "Nigeria announces major economic reforms",
  "Heavy rainfall causes flooding in Lagos",
  "Super Eagles qualify for AFCON finals",
  "New business opportunities opening in Ewatto community"
];

let currentIndex = 0;

function updateTicker() {
  const ticker = document.getElementById("breaking-ticker");
  ticker.textContent = headlines[currentIndex];
  
  // Reset animation
  ticker.style.animation = 'none';
  void ticker.offsetWidth; // trigger reflow
  ticker.style.animation = 'scroll-left 10s linear infinite';
  
  currentIndex = (currentIndex + 1) % headlines.length;
}

// Initialize first headline
updateTicker();

// Change headline every 10 seconds
setInterval(updateTicker, 10000);


