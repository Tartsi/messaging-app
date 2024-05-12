'use strict';

const adminPassword = "adminpassword1234";
// SECURITY NOTIFICATION: The key should be more random and it should not be
// stored here as it is visible to everyone! This leaves the application vulnerable to
// unauthorized access attacks (admin-privileges).

// SOLUTION: The key should be more secure (Capital letters, digits, numbers and specialized characters, also 12 characters long atleast!)
// It should be hashed and salted properly using algorithms specializing in this such as bcrypt - (Just like any other password in this application should be)
// It should not be stored in a visible location. It should be securely stored in the database.

// SECURITY NOTIFICATION: This input check method for password checks is not extensive enough, and leaves an opening for weak passwords.

// SOLUTION: Provide more in-depth password checks that 'force' the user to create strong passwords.
// (Capital letters, digits, numbers and specialized characters, also 12 characters long atleast!)

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
