/* 
    Delete an item from the cart when button is clicked
*/

$('.update-link').click(function(e) {
    let form = $(this).prev('.update-form');
    form.submit();
})

$('.remove-item').click(function(e) {
    // Define the variables to be used in the post method variables
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    let itemId = $(this).attr('id').split('remove_')[1];
    let size = $(this).data('item_size');

    // Define the post variables
    let url = `/cart/remove/${itemId}/`;
    let data = {'csrfmiddlewaretoken': csrftoken, 'item_size': size};

    // Post the url and data to the delete_from_cart view and reload the page
    $.post(url, data)
    .done(function() {
        location.reload();
    });
});