import React, { useContext, useEffect, useState } from 'react';
import axios from 'axios';
import { useNavigate, useParams } from 'react-router-dom';
import { Container, Row, Col, Image } from 'react-bootstrap';
import { CartContext } from "../context/cartContext";
import '../style/ProductDetails.css';
function ProductDetailsPage() {
  const [product, setProduct] = useState(null);
  const [loading, setLoading] = useState(true);
 const { id } = useParams();
  const { addToCart } = useContext(CartContext);
   const navigate = useNavigate();

  useEffect(() => {
    const fetchProduct = async () => {
      try {
        const response = await axios.get(`http://localhost:3005/products/${id}`);
        setProduct(response.data);
        setLoading(false);
      } catch (error) {
        console.error("Error fetching product details:", error);
        setLoading(false);
      }
    };
    fetchProduct();
  }, [id]);

  if (loading) return <div className="text-center mt-5">Loading product details...</div>;
  if (!product) return <div className="text-center mt-5">Product not found.</div>;
    const handleAddToCart = () => {
    addToCart(product);
    navigate("/cart"); 
  };
 return (
    <Container className="container fluid ">
      <Row>
        <Col md={4}>
          <Image className='product-image mt-4' src={product.image_link} alt={product.name} fluid />
        </Col>
        <Col md={6} className="d-flex flex-column justify-content-center">
          <h1>{product.name}</h1>
          <p className="text-muted">{product.description}</p>
          <h3>${product.price}</h3>
          <p><strong>Category:</strong> {product.category}</p>
          <p><strong>Available:</strong> {product.count} items</p>
          <button 
            className="add-to-cart btn btn-warning mt-3"
            onClick={handleAddToCart}
          >
            Add to Cart
          </button>
        </Col>
      </Row>
    </Container>
  );
}

export default ProductDetailsPage;
