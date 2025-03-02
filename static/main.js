function getCookie(c_name) {
    var i, x, y, ARRcookies = document.cookie.split(";");
    for (i = 0; i < ARRcookies.length; i++) {
        x = ARRcookies[i].substr(0, ARRcookies[i].indexOf("="));
        y = ARRcookies[i].substr(ARRcookies[i].indexOf("=") + 1);
        x = x.replace(/^\s+|\s+$/g, "");
        if (x == c_name) {
            return unescape(y);
        }
    }
}

function setCookie(c_name, value, exdays) {
    var exdate = new Date();
    exdate.setDate(exdate.getDate() + exdays);
    var c_value = escape(value) + ((exdays == null) ? "" : "; expires=" + exdate.toUTCString());
    document.cookie = c_name + "=" + c_value;
}

function checkForm() {
    // Get the input values
    const originInput = document.getElementById('id_origin').value.trim();
    const destinationInput = document.getElementById('id_destination_state').value.trim();
    
    // Check if both fields are empty
    if (!originInput && !destinationInput) {
        alert("Please fill in at least one search field");
        return false;
    }
    
    // Check for Elon Musk
    if (originInput.toLowerCase().includes('elon musk') || 
        destinationInput.toLowerCase().includes('elon musk')) {
        alert("He's not here");
        return false;
    }
    
    return true;
}

function checkFirstVisit() {
    // Check if we have a cookie indicating previous visit
    const visited = getCookie("visited");
    
    if (!visited) {
        // First time visitor
        setCookie("visited", "true", 365);
        
        // Show welcome message
        showWelcomeMessage();
    }
}

function showWelcomeMessage() {
    // Create welcome message elements
    const welcomeOverlay = document.createElement('div');
    welcomeOverlay.className = 'welcome-overlay';
    
    const welcomeBox = document.createElement('div');
    welcomeBox.className = 'welcome-box';
    welcomeBox.innerHTML = `
        <h2>Welcome to CarpoolBuddyRides!</h2>
        <p>Find and share rides with other event attendees.</p>
        <button onclick="closeWelcome()">Get Started</button>
    `;
    
    welcomeOverlay.appendChild(welcomeBox);
    document.body.appendChild(welcomeOverlay);
}

function closeWelcome() {
    const overlay = document.querySelector('.welcome-overlay');
    if (overlay) {
        overlay.remove();
    }
}

// Run the check when the page loads
window.onload = function() {
    checkFirstVisit();
};
