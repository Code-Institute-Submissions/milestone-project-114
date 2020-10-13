let stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
let clientSecret = $('#id_client_secret').text().slice(1, -1);
let stripe = Stripe(stripePublicKey);
const url = "{% url 'subscribe:create_subscription' %}"

if (document.getElementById('card-element')) {
    let elements = stripe.elements();

    // Element style
    let style = {
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

    card = elements.create('card', { style: style });

    card.mount('#card-element');
}

// Mount the subscription choice to the payment form
function planSelect(name, price, priceId) {
    var inputs = document.getElementsByTagName('input');

    for(var i = 0; i<inputs.length; i++){
        inputs[i].checked = false;
        if(inputs[i].name== name){

            inputs[i].checked = true;
        }
    }

    var n = document.getElementById('plan');
    var p = document.getElementById('price');
    var pid = document.getElementById('priceId');
    n.innerHTML = name;
    p.innerHTML = price;
    pid.innerHTML = priceId;
    document.getElementById("submit").disabled = false;
}


// Handle and display card errors
card.addEventListener('change', function(event) {
    let errorDiv = document.getElementById('subscribe-card-errors');

    if (event.error) {
        let html = `
            <span class="icon card-error-icon" role="alert">
                <i class="fa fa-times"></i>
            </span>

            <span>${event.error.message}</span>
        `;

        $(errorDiv).html(html);
    } else {
        errorDiv.textContext = '';
    }
});

//------------------------------------------------------ Form Submit
function stripePaymentMethodHandler(result, email) {
    if (result.error) {
        let errorDiv = document.getElementById('subscribe-card-errors');
    let html = `
            <span class="icon card-error-icon" role="alert">
                <i class="fa fa-times"></i>
            </span>

            <span>${event.error.message}</span>
        `;

        $(errorDiv).html(html);
    } else {
    const paymentParams = {
        email: email,
        plan_id: getSelectedPlanId(),
        payment_method: result.paymentMethod.id,
    };
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
        },
        credentials: 'same-origin',
        body: JSON.stringify(paymentParams),
    }).then(function(response) {
        return response.json(); 
    }).then(function(result) {
        // todo: check and process subscription status based on the response
    }).catch(function (error) {
        // more error handling
    });
    }
};