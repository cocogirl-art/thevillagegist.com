// List of breaking news headlines
const headlines = [
    "Nigeria announces major economic reforms",
    "Heavy rainfall causes flooding in Lagos",
    "Super Eagles qualify for AFCON finals",
    "New business opportunities opening in Ewatto community"
];

let currentIndex = 0; // Start with the first headline

document.addEventListener("DOMContentLoaded", () => {
    const tickerContainer = document.getElementById("breaking-ticker");

    if (tickerContainer) {
        // Function to update headline
        function updateTicker() {
            tickerContainer.innerHTML = `<marquee behavior="scroll" direction="left" scrollamount="6">${headlines[currentIndex]}</marquee>`;
            currentIndex = (currentIndex + 1) % headlines.length; // Loop through headlines
        }

        // Show first headline
        updateTicker();

        // Change headline every 6 seconds
        setInterval(updateTicker, 6000);
    }
});
