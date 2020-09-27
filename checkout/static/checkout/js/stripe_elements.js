let stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
let clientSecret = $('#id_client_secret').text().slice(1, -1);
let stripe = Stripe(stripePublicKey);
let elements = stripe.elements();

var style = {
  base: {
    color: '#000000',
    fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
    fontSmoothing: 'antialiased',
    fontSize: '16px',
    '::placeholder': {
      color: '#aab7c4'
    }
  },
  invalid: {
    color: '#dc3545',
    iconColor: '#dc3545'
  }
};

let card = elements.create('card', {style: style});

card.mount('#card-element');

// Handle realtime validation errors on the card element
card.addEventListener('change', function(event) {
    let errorDiv = document.getElementById('card-errors');

    if (event.error) {
        let html = `
            <span class="icon" role="alert">
                <i class="fa fa-times"></i>
            </span>

            <span>${event.error.message}</span>
        `

        $(errorDiv).html(html);
    } else {
        errorDiv.textContext = '';
    }
});

// Handle form submit

var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({'disabled': true});
    $('#submit-button').attr('disabled', true);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
        card: card,
    }
    }).then(function(result) {
        let errorDiv = document.getElementById('card-errors');

        if (result.error) {
            let html = `
                <span class="icon" role="alert">
                    <i class="fa fa-times"></i>
                </span>

                <span>${event.error.message}</span>
            `

            $(errorDiv).html(html);
            card.update({'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});