import React from "react";
import "../style/OrderSucess.css";
import Header from "../components/Header";
function OrderSuccessPage() {
  return (
    <div>
      <Header />
        <div className="d-flex justify-content-center align-items-center vh-100  text-black" >
        
      <h1>Order Shipped Successfully</h1>
    </div>
    </div>
  );
}

export default OrderSuccessPage;
