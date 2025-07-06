document.addEventListener('DOMContentLoaded', () => {
  const cart = JSON.parse(localStorage.getItem('cart')) || {};

  // Update cart count on header
  updateCartCount();

  document.querySelectorAll('.add-to-cart-btn').forEach(button => {
    button.addEventListener('click', function () {
      const productId = this.dataset.productId;

      if (cart[productId]) {
        cart[productId].quantity += 1;
      } else {
        const productName = this.dataset.name;
        const price = parseFloat(this.dataset.price);
        cart[productId] = { name: productName, quantity: 1, price };
      }

      localStorage.setItem('cart', JSON.stringify(cart));
      updateCartCount();
      alert("Item added to cart!");
    });
  });
});

function updateCartCount() {
  const cart = JSON.parse(localStorage.getItem('cart')) || {};
  const count = Object.values(cart).reduce((sum, item) => sum + item.quantity, 0);
  const cartCounter = document.querySelector('.cart-counter');
  if (cartCounter) cartCounter.textContent = count;
}
