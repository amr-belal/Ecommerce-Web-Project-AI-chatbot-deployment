import React, { useContext } from "react";
import { CartContext } from "../context/cartContext";
import { useNavigate } from "react-router-dom";
import '../style/CartPage.css';
function CartPage() {
  const { cart, updateQuantity, clearCart } = useContext(CartContext);
  const navigate = useNavigate();

  const total = cart.reduce((sum, item) => sum + item.price * item.quantity, 0);

  const handleBuyNow = () => {
    clearCart();
    navigate("/order-success");
  };

  return (
    <div className="container mt-5">
      <h2 className="mb-4 text-center">Your Cart</h2>
      {cart.length === 0 ? (
        <p>No items in cart</p>
      ) : (
        <>
          {cart.map(item => (
            <div key={item.id} className="d-flex justify-content-between align-items-center border-bottom py-3">
              <span>{item.name} - ${item.price}</span>
              <div>
                <button onClick={() => updateQuantity(item.id, -1)}>-</button>
                <span className="mx-2">{item.quantity}</span>
                <button onClick={() => updateQuantity(item.id, 1)}>+</button>
              </div>
            </div>
          ))}
          <h4 className="mt-3">Total Amount: ${total}</h4>
          <button className="button-submit btn mt-3 d-flex align-items-center justify-content-center" onClick={handleBuyNow}>Buy Now</button>
        </>
      )}
    </div>
  );
}

export default CartPage;
