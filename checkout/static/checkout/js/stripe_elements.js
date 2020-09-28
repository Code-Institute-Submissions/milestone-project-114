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
    $('payment-form').fadeToggle(100);
    $('loading-overlay').fadeToggle(100);

    let saveInfo = Boolean($('#id-save-info').attr('checked'));
    let csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    let postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': client_secret,
        'save_info': saveInfo
    }
    let url = '/checkout/cache_checkout_data/';

    $.post(url, postData).done(function() {
        stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
            billing_details: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                email: $.trim(form.email.value),
                address: {
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.town_or_city.value),
                    country: $.trim(form.country.value),
                    county: $.trim(form.county.value),
                }
            }
        },
        delivery: {
            name: $.trim(form.full_name.value),
            phone: $.trim(form.phone_number.value),
            email: $.trim(form.email.value),
            address: {
                line1: $.trim(form.street_address1.value),
                line2: $.trim(form.street_address2.value),
                city: $.trim(form.town_or_city.value),
                country: $.trim(form.country.value),
                postcode: $.trim(form.postcode.value),
                county: $.trim(form.county.value),
            }
        },
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
                $('payment-form').fadeToggle(100);
                $('loading-overlay').fadeToggle(100);
                card.update({'disabled': false});
                $('#submit-button').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function() {
        location.reload();
    })
});