document.addEventListener('DOMContentLoaded', function() {
    var cartToggler = document.getElementById('cart-toggler');
    var cart = document.querySelector('.cart');

    cartToggler.addEventListener('click', function() {
        // Переключаем класс show для корзины, чтобы показать или скрыть ее с анимацией
        cart.classList.toggle('show');
    });
});
