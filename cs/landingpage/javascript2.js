// Function to handle course search
function searchCourse() {
    let query = document.getElementById('searchInput').value;
    if (query.trim() === "") {
        alert("Please enter a course name.");
        return false;
    }
    alert("Searching for: " + query);
    return false;
}

// Function to open the registration popup
function openRegister() {
    document.getElementById("registerPopup").style.display = "flex";
}

// Function to close the registration popup
function closeRegister() {
    document.getElementById("registerPopup").style.display = "none";
}
