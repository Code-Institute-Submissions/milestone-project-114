let stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
let stripe = Stripe(stripePublicKey);
let elements = stripe.elements();

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

let cardElement = elements.create("card", { style: style });
cardElement.mount("#subscribe-card-element");

cardElement.on('change', showCardError);

function showCardError(event) {
  let displayError = document.getElementById('subscribe-card-errors');
  if (event.error) {
    displayError.textContent = event.error.message;
  } else {
    displayError.textContent = '';
  }
}

let form = document.getElementById('subscription-form');
​
form.addEventListener('submit', function (ev) {
  ev.preventDefault();
​
  // If a previous payment was attempted, get the latest invoice
  const latestInvoicePaymentIntentStatus = localStorage.getItem(
    'latestInvoicePaymentIntentStatus'
  );
​
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
​
function createPaymentMethod({ card, isPaymentRetry, invoiceId }) {
  // Set up payment method for recurring usage
​
  stripe
    .createPaymentMethod({
      type: 'card',
      card: card,
    })
    .then((result) => {
      if (result.error) {
        displayError(result);
      } else {
        if (isPaymentRetry) {
          // Update the payment method and retry invoice payment
          retryInvoiceWithNewPaymentMethod({
            customerId: customerId,
            paymentMethodId: result.paymentMethod.id,
            invoiceId: invoiceId,
            priceId: priceId,
          });
        } else {
          // Create the subscription
          createSubscription({
            customerId: customerId,
            paymentMethodId: result.paymentMethod.id,
            priceId: priceId,
          });
        }
      }
    });
}

function createSubscription({ customerId, paymentMethodId, priceId }) {
  return (
    fetch('/create-subscription', {
      method: 'post',
      headers: {
        'Content-type': 'application/json',
      },
      body: JSON.stringify({
        customerId: customerId,
        paymentMethodId: paymentMethodId,
        priceId: priceId,
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
          priceId: priceId,
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
        // An error has happened. Display the failure to the user here.
        // We utilize the HTML element we created.
        showCardError(error);
      })
  );
}
