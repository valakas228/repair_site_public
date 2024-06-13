document.addEventListener('DOMContentLoaded', function() {
    var cartToggler = document.getElementById('cart-toggler');
    var cart = document.querySelector('.cart');

    cartToggler.addEventListener('click', function() {
        cart.classList.toggle('show');
    });
});