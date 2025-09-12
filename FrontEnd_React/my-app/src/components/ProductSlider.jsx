// src/components/ProductSlider.jsx
import React, { useEffect, useState } from 'react';
import Slider from 'react-slick';
import axios from 'axios';
import { Container, Card } from 'react-bootstrap';
import '../style/TopSellingSection.css';

function ProductSlider({ type }) { // <-- Accepts a 'type' prop
    const [products, setProducts] = useState([]);
    const [title, setTitle] = useState('');
    const [subtitle, setSubtitle] = useState('');

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get("http://localhost:3005/products");
                let fetchedProducts = [];
                if (type === 'new') {
                    fetchedProducts = response.data.sort((a,b)=>b.count - a.count);
                    setTitle("New Collection");
                    setSubtitle("Discover the Latest Scents of the Season");
                } else if (type === 'topSelling') {
                    fetchedProducts = response.data.sort((a, b) => b.count - a.count).slice(0, 3);
                    setTitle("Top-Selling Perfumes");
                    setSubtitle("The Most Popular and Best Scents of the Year Collection");
                }
                setProducts(fetchedProducts);
            } catch (error) {
                console.error(`Error fetching ${type} products:`, error);
            }
        };
        fetchData();
    }, [type]); // Dependency on 'type' ensures data is re-fetched when the prop changes.

    const settings = {
        // Your slider settings remain the same
        dots: true,
        infinite: true,
        speed: 500,
        slidesToShow: 3,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 3000,
        responsive: [
            { breakpoint: 1024, settings: { slidesToShow: 2 } },
            { breakpoint: 600, settings: { slidesToShow: 1 } }
        ]
    };

    return (
        <div className="product-slider-section">
            <Container>
                <div className="text-center mb-5">
                    <h2 className="section-title">{title}</h2>
                    <p className="section-subtitle">{subtitle}</p>
                </div>
                {products.length > 0 ? (
                    <Slider {...settings}>
                        {products.map((product) => (
                            <div key={product.id} className="slider-item-wrapper">
                                <Card className="slider-card h-100 border-0 text-center">
                                    <Card.Img variant="top" src={product.image_link} alt={product.name} className="product-image rounded-circle mx-auto" />
                                    <Card.Body>
                                        <Card.Title className="product-name">{product.name}</Card.Title>
                                        <Card.Text className="product-price">${product.price}</Card.Text>
                                    </Card.Body>
                                </Card>
                            </div>
                        ))}
                    </Slider>
                ) : (
                    <div className="text-center">Loading...</div>
                )}
            </Container>
        </div>
    );
}

export default ProductSlider;