$(document).ready(function() {
    $("form.add-to-cart-form").submit(function(event) {
        event.preventDefault();

        var form = $(this);
        var productId = form.find('.add-to-cart-btn').data('product-id');

        $.ajax({
            url: form.attr('action'),
            method: form.attr('method'),
            data: form.serialize(),
            success: function(response) {
                $("#cart-total").text(response.total_items);
                $("#cart-items-container").html(response.cart_items_html);

                // Обновляем значение количества товаров на кнопке "+"
                var quantity = response.cart_items.find(item => item.product_id === productId).quantity;
                form.find('.add-to-cart-btn').siblings('.mx-2').text(quantity);
            }
        });
    });

    $("form.remove-from-cart-form").submit(function(event) {
        event.preventDefault();

        var form = $(this);
        var productId = form.find('.remove-from-cart-btn').data('product-id');

        $.ajax({
            url: form.attr('action'),
            method: form.attr('method'),
            data: form.serialize(),
            success: function(response) {
                $("#cart-total").text(response.total_items);
                $("#cart-items-container").html(response.cart_items_html);

                // Обновляем значение количества товаров на кнопке "-"
                var quantity = response.cart_items.find(item => item.product_id === productId).quantity;
                form.find('.remove-from-cart-btn').siblings('.mx-2').text(quantity);
            }
        });
    });
});
