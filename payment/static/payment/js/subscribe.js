const stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
const stripe = Stripe(stripePublicKey);
const elements = stripe.elements();
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

function planSelect(name, price, priceId) {
    let inputs = document.getElementsByTagName('input');

    for(let i = 0; i<inputs.length; i++){
        inputs[i].checked = false;
        if(inputs[i].name== name){

            inputs[i].checked = true;
        }
    }

    let n = document.getElementById('plan');
    let p = document.getElementById('price');
    let pid = document.getElementById('priceId');
    n.innerHTML = name;
    p.innerHTML = price;
    pid.innerHTML = priceId;
    document.getElementById("submit").disabled = false;
}

let style = {
    base: {
        color: "#32325d",
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: "antialiased",
        fontSize: "16px",
        "::placeholder": {
        color: "#aab7c4"
        }
    },
    invalid: {
        color: "#fa755a",
        iconColor: "#fa755a"
    }
};

let card = elements.create("card", { style: style });
card.mount("#subscribe-card-element");
card.on('change', showCardError);

function showCardError(event) {
    let displayError = document.getElementById('subscribe-card-errors');
    if (event.error) {
        displayError.textContent = event.error.message;
    } else {
        displayError.textContent = '';
    }
}

let form = document.getElementById('subscription-form');

form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    changeLoadingState(true);

    // If a previous payment was attempted, get the latest invoice
    const latestInvoicePaymentIntentStatus = localStorage.getItem(
    'latestInvoicePaymentIntentStatus'
    );

    if (latestInvoicePaymentIntentStatus === 'requires_payment_method') {
    const invoiceId = localStorage.getItem('latestInvoiceId');
    const isPaymentRetry = true;
    // create new payment method & retry payment on invoice with new payment method
    createPaymentMethod({
        card,
        isPaymentRetry,
        invoiceId,
    });
    } else {
    // create new payment method & create subscription
    createPaymentMethod({ card });
    }
});

function createPaymentMethod({ card, isPaymentRetry, invoiceId }) {
  // Set up payment method for recurring usage
    stripe.createPaymentMethod({
            type: 'card',
            card: card,
        })
    .then((result) => {
        if (result.error) {
            displayError(result);
            changeLoadingState(false);
        } else {
            if (isPaymentRetry) {
            // Update the payment method and retry invoice payment
            retryInvoiceWithNewPaymentMethod({
                paymentMethodId: result.paymentMethod.id,
                invoiceId: invoiceId,
                priceId: document.getElementById("priceId").innerHTML,
            });
            } else {
                // Create the subscription
                createSubscription({
                    paymentMethodId: result.paymentMethod.id,
                    priceId: document.getElementById("priceId").innerHTML,
                });
            }
        }
    });
}

function createSubscription({paymentMethodId, priceId }) {
    return (
        fetch(create_subscription_url, {
        method: 'post',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            paymentMethodId: paymentMethodId,
            priceId: document.getElementById("priceId").innerHTML,
        }),
        })
        .then((response) => {
            return response.json();
        })
        // If the card is declined, display an error to the user.
        .then((result) => {
            if (result.error) {
            // The card had an error when trying to attach it to a customer.
            throw result;
            }
            return result;
        })
        // Normalize the result to contain the object returned by Stripe.
        // Add the additional details we need.
        .then((result) => {
            return {
            paymentMethodId: paymentMethodId,
            priceId: document.getElementById("priceId").innerHTML,
            subscription: result,
            };
        })
        // Some payment methods require a customer to be on session
        // to complete the payment process. Check the status of the
        // payment intent to handle these actions.
        .then(handlePaymentThatRequiresCustomerAction)
        // If attaching this card to a Customer object succeeds,
        // but attempts to charge the customer fail, you
        // get a requires_payment_method error.
        .then(handleRequiresPaymentMethod)
        // No more actions required. Provision your service for the user.
        .then(onSubscriptionComplete)
        .catch((error) => {
            changeLoadingState(false);
            // An error has happened. Display the failure to the user here.
            // We utilize the HTML element we created.
            showCardError(error);
        })
    );
}

function handlePaymentThatRequiresCustomerAction({
    subscription,
    invoice,
    priceId,
    paymentMethodId,
    isRetry,
    }) {
    if (subscription && subscription.status === 'active') {
        // Subscription is active, no customer actions required.
        return { subscription, priceId, paymentMethodId };
    }

    // If it's a first payment attempt, the payment intent is on the subscription latest invoice.
    // If it's a retry, the payment intent will be on the invoice itself.
    let paymentIntent = invoice ? invoice.payment_intent : subscription.latest_invoice.payment_intent;

    if (
        paymentIntent.status === 'requires_action' ||
        (isRetry === true && paymentIntent.status === 'requires_payment_method')
    ) {
        return stripe
        .confirmCardPayment(paymentIntent.client_secret, {
            payment_method: paymentMethodId,
        })
        .then((result) => {
            if (result.error) {
            // Start code flow to handle updating the payment details.
            // Display error message in your UI.
            // The card was declined (i.e. insufficient funds, card has expired, etc).
            throw result;
            } else {
            if (result.paymentIntent.status === 'succeeded') {
                // Show a success message to your customer.
                // There's a risk of the customer closing the window before the callback.
                // We recommend setting up webhook endpoints later in this guide.
                return {
                priceId: document.getElementById("priceId").innerHTML,
                subscription: subscription,
                invoice: invoice,
                paymentMethodId: paymentMethodId,
                };
            }
            }
        })
        .catch((error) => {
            displayError(error);
            changeLoadingState(false);
        });
    } else {
        // No customer action needed.
        return { subscription, priceId, paymentMethodId };
    }
}

function handleRequiresPaymentMethod({
    subscription,
    paymentMethodId,
    priceId,
    }) {
    if (subscription.status === 'active') {
        // subscription is active, no customer actions required.
        return { subscription, priceId, paymentMethodId };
    } else if (
        subscription.latest_invoice.payment_intent.status ===
        'requires_payment_method'
    ) {
        // Using localStorage to manage the state of the retry here,
        // feel free to replace with what you prefer.
        // Store the latest invoice ID and status.
        localStorage.setItem('latestInvoiceId', subscription.latest_invoice.id);
        localStorage.setItem(
        'latestInvoicePaymentIntentStatus',
        subscription.latest_invoice.payment_intent.status
        );
        throw { error: { message: 'Your card was declined.' } };
    } else {
        return { subscription, priceId, paymentMethodId };
    }
}

function onSubscriptionComplete(result) {
    // Payment was successful.
    if (result.subscription.status === 'active' || 'paid') {
        window.location.href = on_subscription_complete_url;
        // Change your UI to show a success message to your customer.
        // Call your backend to grant access to your service based on
        // `result.subscription.items.data[0].price.product` the customer subscribed to.
    }
}

function retryInvoiceWithNewPaymentMethod({
    paymentMethodId,
    invoiceId,
    priceId
    }) {
    return (
        fetch(retry_invoice_url, {
        method: 'post',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            paymentMethodId: paymentMethodId,
            invoiceId: invoiceId,
        }),
        })
        .then((response) => {
            return response.json();
        })
        // If the card is declined, display an error to the user.
        .then((result) => {
            if (result.error) {
            // The card had an error when trying to attach it to a customer.
            throw result;
            }
            return result;
        })
        // Normalize the result to contain the object returned by Stripe.
        // Add the additional details we need.
        .then((result) => {
            return {
            // Use the Stripe 'object' property on the
            // returned result to understand what object is returned.
            invoice: result,
            paymentMethodId: paymentMethodId,
            priceId: document.getElementById("priceId").innerHTML,
            isRetry: true,
            };
        })
        // Some payment methods require a customer to be on session
        // to complete the payment process. Check the status of the
        // payment intent to handle these actions.
        .then(handlePaymentThatRequiresCustomerAction)
        // No more actions required. Provision your service for the user.
        .then(onSubscriptionComplete)
        .catch((error) => {
            changeLoadingState(false);
            // An error has happened. Display the failure to the user here.
            // We utilize the HTML element we created.
            displayError(error);
        })
    );
}

function changeLoadingState(isLoading) {
    if (isLoading) {
        document.querySelector('#button-text').classList.add('hidden');
        document.querySelector('#spinner').classList.remove('hidden');
        document.querySelector('#subscription-form button').disabled = true;
    } else {
        document.querySelector('#button-text').classList.remove('hidden');
        document.querySelector('#spinner').classList.add('hidden');
        document.querySelector('#subscription-form button').disabled = false;
    }
}