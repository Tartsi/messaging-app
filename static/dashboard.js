'use strict';

function showLoggedInUser() {
    alert("Logged in!");
}

function userNotFound() {
    alert("User you are trying to send message to not found!");
}

function messageSent() {
    alert("Message sent succesfully!");
}

function checkMessage() {

    // Check if trying to send message to yourself

    let receiverUsername = document.getElementById("receivername").value;

    let username = document.getElementById("h1user").textContent.split("Welcome, ")[1];
    username = username.trim();

    if (username == receiverUsername.trim()) {
        alert("Cannot send message to yourself!");
        document.getElementById("receivername").value = "";
        document.getElementById("messagecontent").value = "";
        return false;
    }

    // SECURITY NOTIFICATION: This input check method is insufficient and thus a security issue.
    // There is no message content sanitization happening, thus the form is subject to potential
    // XSS vulnerabilities as it can be used to send malicious content.

    // SOLUTION: Use more indepth input checks in the JavaScript-file

    // Example:

    // maliciousChars = ["<", ">", "</script"... etc.];

    // for (let i = 0; i < maliciousChars.length; i++) {
    //     if (messageContent.includes(maliciousChars[i])) {
    //         alert("Malicious content detected!");
    //         return false;
    //     }
    // }

    // Also add a security check on the backend to routes.py file!
    // This example is on line #171 and onward!

    return true;
}
