import React, { useContext } from 'react'
import '../style/ProductGalleryPage.css'
import { CartContext } from "../context/cartContext";
import { useNavigate } from 'react-router-dom';

function ProductCard({ product, onViewDetails }) {
  const { addToCart } = useContext(CartContext);
  const navigate = useNavigate();
  return (
    <div className="ProductCard card rounded-0 shadow-sm">
      <img 
        src={product.image_link} 
        className="card-img-top" 
        alt={product.name} 
      />

      <div className="card-body">
        <h5 className="card-title">{product.name}</h5>
        <p className="card-text">${product.price}</p>

        <div className="d-flex justify-content-between">
        
          <button 
            className="button-details btn btn-primary"
            onClick={() => onViewDetails(product.id)}
          >
            View Details <i className="bi bi-eye ms-2"></i>
          </button>

        
          <button
            className="add button-add-to-cart btn  d-flex align-items-center justify-content-center mx-2"
            style={{ width: "45px", height: "45px", borderRadius: "50%" }}
            onClick={() => {
                addToCart(product);
                console.log("Product added to cart:", product);
            }}
          >
            <i className="bi bi-plus-lg"></i>
          </button>

          <button
            className="add button-add-to-cart btn  d-flex align-items-center justify-content-center mx-1"
            style={{ width: "45px", height: "45px", borderRadius: "50%" }}
            onClick={() => {
                navigate("/cart"); 
            }}
          >
            <i className="bi bi-cart"></i>
          </button>
        </div>
      </div>
    </div>
  );
}

export default ProductCard;
