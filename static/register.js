'use strict';

const adminPassword = "adminpassword1234";
// SECURITY NOTIFICATION: The key should be more random.
// In this form this is more of a "theoretical" and not a "realistic" security flaw.

// SECURITY NOTIFICATION: This input check method is insufficient and thus a security issue.
// These password checks are simply not good enough. Also there are no limits on the number
// of characters one can input, and no sanitization as to what those characteres are.

function inputCheck() {


    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;
    let confirmPassword = document.getElementById('confirm-password').value;
    let adminPass = document.getElementById('admin-password').value;

    if (username.length < 4) {
        alert('Username must be at least 4 characters long.');
        username.value = "";
        password.value = "";
        confirmPassword.value = "";
        adminPass.value = "";
        return false;
    }

    let hasNumbers = /\d/;

    if (password.length < 5) {
        alert('Password must be at least 5 characters long.');
        username.value = "";
        password.value = "";
        confirmPassword.value = "";
        adminPass.value = "";
        return false;
    }

    if (!hasNumbers.test(password)) {
        alert("Password must contain at least one number.");
        username.value = "";
        password.value = "";
        confirmPassword.value = "";
        adminPass.value = "";
        return false;
    }

    if (confirmPassword !== password) {
        alert("Password and confirm password do not match.");
        username.value = "";
        password.value = "";
        confirmPassword.value = "";
        adminPass.value = "";
        return false;
    }

    let adminCheckbox = document.getElementById("admin-checkbox");

    if (adminCheckbox.checked) {

        if (adminPassword !== adminPass) {

            alert("Admin password is incorrect!");
            username.value = "";
            password.value = "";
            confirmPassword.value = "";
            adminPass.value = "";
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