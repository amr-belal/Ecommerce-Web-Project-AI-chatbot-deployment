import React, { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom"; // لازم تكون v6
import { Button, Card, Container } from "react-bootstrap";
import "../style/ProductGalleryPage.css";
import ProductCard from "../components/ProductCard";

function ProductDetailsPage() {
  const [products, setProducts] = useState([]);
  const [filteredProducts, setFilteredProducts] = useState([]);
  const [activeFilter, setActiveFilter] = useState("All Perfume");
  const navigate = useNavigate();

  useEffect(() => {
    const fetchProduct = async () => {
      try {
        const response = await axios.get("http://localhost:3005/products");
        setProducts(response.data);
        setFilteredProducts(response.data);
      } catch (error) {
        console.error("Error fetching products:", error);
      }
    };
    fetchProduct();
  }, []);

  const handleFilterClick = (filter) => {
    setActiveFilter(filter);
    let tempProducts = [];

    if (filter === "All Perfume") {
      tempProducts = products;
    }  else if (filter === "Men") {
      tempProducts = [...products].filter((product)=>product.category === "men");
    }
    else if (filter === "Women") {
      tempProducts = [...products].filter((product)=>product.category === "women");
    }

    setFilteredProducts(tempProducts);
  };

  const handleViewDetails = (id) => {
    navigate(`/products/${id}`);
  };

  return (
   
<div className="main-page-container">
      <div className="container text-center">
        <h2 className="mb-4">Grab Your Signature Scent Today!</h2>

        <div className="d-flex justify-content-center gap-2 mb-4">
          {["All Perfume", "Men", "Women"].map((filter) => (
            <button 
              key={filter}
              className={`filterButton btn btn-dark rounded-pill px-4 ${
                activeFilter === filter ? "active" : ""
              }`}
              onClick={() => handleFilterClick(filter)}
            >
              {filter}
            </button>
          ))}
        </div>

        <div className="row justify-content-center">
          {filteredProducts.map((product) => (
            <div className="col-auto" key={product.id}>
              <ProductCard 
                product={product} 
                onViewDetails={handleViewDetails} 
              />
            </div>
          ))}
        </div>

        
        {filteredProducts.length === 0 && (
          <div className="text-center mt-5">
            <p className="text-muted">No products found for this category.</p>
          </div>
        )}
      </div>
    </div>

  );
}

export default ProductDetailsPage;
