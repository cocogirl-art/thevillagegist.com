alert("Welcome to TheVillageGist News Network!");
// Get today's date
const today = new Date();

// Format the date
const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
const formattedDate = today.toLocaleDateString('en-US', options);

// Display it in the element
document.getElementById("current-date").textContent = formattedDate;
