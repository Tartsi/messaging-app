'use strict';

function showLoginMessage() {
    alert("Welcome to the administration page.");
}

function confirmAction(data) {

    let infoMessage = "";

    if (data.includes("delete")) {
        infoMessage = "Are you sure you want to delete this user?";
    } else {
        infoMessage = "Are you sure you want to ban this user?";
    }

    if (confirm(infoMessage)) {
        window.location.href = data;
    }

    return;
}
