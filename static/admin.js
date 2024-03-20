'use strict';

function confirmAction(url) {

    if (confirm("Are you sure you want to delete this user?")) {
        window.location.href = url;
    }

    return;
}
