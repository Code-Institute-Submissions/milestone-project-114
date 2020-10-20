const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

function cancelSubscription() {
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
    });
}