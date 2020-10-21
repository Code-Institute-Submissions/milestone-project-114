/*
    Cancel the subscription
*/

// Define the csrf token
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

// Shows the cancellation response
function subscriptionCancelled() {
    document.querySelector('#subscription-cancelled').classList.remove('hidden');
    document.querySelector('#cancel-button').classList.add('hidden');
}

// Handle the subscription cancellation
function cancelSubscription() {
    // Fetch the url and post the current subscritpion Id to be cancelled
    return fetch(cancel_subscription_url, {
        method: 'post',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
        subscriptionId: subscriptionId,
        }),
    })
    .then(response => {
    return response.json();
    })
    .then(cancelSubscriptionResponse => {
        // Display to the user that the subscription has been cancelled.
        return subscriptionCancelled(cancelSubscriptionResponse);
    });
}