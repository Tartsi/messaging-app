'use strict';

const adminPassword = "adminpassword1234";
// SECURITY NOTIFICATION: The key should be more random and it should not be
// stored here as it is visible to everyone! This leaves the application vulnerable to
// unauthorized access attacks (admin-privileges).

// SECURITY NOTIFICATION: This input check method is insufficient and thus a security issue.
// Password checks are not extensive enough, they leave openings for weak passwords.
// No limits on the number of characters one can input, and no sanitization as to what the characters are.
// Only client-side validation exists.

function inputCheck() {


    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;
    let confirmPassword = document.getElementById('confirm-password').value;
    let adminPass = document.getElementById('admin-password').value;

    if (username.length < 4) {
        alert('Username must be at least 4 characters long.');
        document.getElementById('username').value = "";
        document.getElementById('password').value = "";
        document.getElementById('confirm-password').value = "";
        document.getElementById('admin-password').value = "";
        return false;
    }

    let hasNumbers = /\d/;

    if (password.length < 5) {
        alert('Password must be at least 5 characters long.');
        document.getElementById('username').value = "";
        document.getElementById('password').value = "";
        document.getElementById('confirm-password').value = "";
        document.getElementById('admin-password').value = "";
        return false;
    }

    if (!hasNumbers.test(password)) {
        alert("Password must contain at least one number.");
        document.getElementById('username').value = "";
        document.getElementById('password').value = "";
        document.getElementById('confirm-password').value = "";
        document.getElementById('admin-password').value = "";
        return false;
    }

    if (confirmPassword !== password) {
        alert("Password and confirm password do not match.");
        document.getElementById('username').value = "";
        document.getElementById('password').value = "";
        document.getElementById('confirm-password').value = "";
        document.getElementById('admin-password').value = "";
        return false;
    }

    let adminCheckbox = document.getElementById("admin-checkbox");

    if (adminCheckbox.checked) {

        if (adminPassword !== adminPass) {

            alert("Admin password is incorrect!");
            document.getElementById('username').value = "";
            document.getElementById('password').value = "";
            document.getElementById('confirm-password').value = "";
            document.getElementById('admin-password').value = "";
            return false;

        }

    }

    return true;
}

function adminPrompt() {

    let adminCheckbox = document.getElementById("admin-checkbox");
    let adminPassword = document.getElementById("admin-password");
    let passwordDiv = document.getElementById("admin-pass-div");

    if (adminCheckbox.checked) {
        passwordDiv.style.display = "block";
    } else {
        adminPassword.value = "";
        passwordDiv.style.display = "none";
    }

}

function showErrorMessage() {
    alert("Username already in use!");
}
