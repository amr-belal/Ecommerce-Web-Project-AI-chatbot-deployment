import React, { use, useEffect, useState } from 'react'
// import productsData  from '../../../server/data.json';
import axios from 'axios';
import '../style/TopSellingSection.css';
import { Container } from 'react-bootstrap';
function TopSellingSection() {
    const [topProducts, setTopProducts] = useState([]);
    useEffect(() => {
        const fetchTopSellingProducts = async () => {
            const response= await axios.get('http://localhost:3005/products');
            const allProducts = response.data;

            const sortedProducts = allProducts.sort((a,b)=>b.count - a.count);
            const top3 =sortedProducts.slice(0,3);
            setTopProducts(top3);
            console.log(top3);
            

        }
        fetchTopSellingProducts();

    }, []); // [] for only one time 

  return (
    <Container fluid className="top-selling-section">
    
    <div className=" perfume-nav py-2"> 
      <ul className="nav justify-content-center">
        <li className="nav-item mx-4">
          <span className="nav-link">Fragrance Defined</span>
        </li>
        <li className="separator mx-4">✶</li>
        <li className="nav-item">
          <span className="nav-link mx-4">Scent Of Elegance</span>
        </li>
        <li className="separator mx-4">✶</li>
        <li className="nav-item">
          <span className="nav-link mx-4">Perfume Essence</span>
        </li>
        <li className="separator mx-4">✶</li>
        <li className="nav-item">
          <span className="nav-link mx-4">Aroma Inspiration</span>
        </li>
        <li className="separator mx-4">✶</li>
        <li className="nav-item">
          <span className="nav-link mx-4 ">Signature Scent</span>
        </li>
      </ul>
      
    </div>

     <div className=" container my-4 ">
            <div className="HeaderTitle text-center mb-5">
                <h2 className="perfume-main-title">
              Top-Selling Perfumes -
            </h2>
            
            <h3 className="perfume-subtitle">
              The Most Popular 
              <span className="perfume-script-text">
                and Best
              </span>
            </h3>
            
            <h2 className="perfume-collection-title">
              Scents of the Year Collection
            </h2>
            </div>
            
            <div className="row justify-content-center">
                {topProducts.map((product) => (
                    <div className="col-md-4 mb-4 d-flex justify-content-center" key={product.id}>
                        <div className="card shadow-sm border-1" style={{height: '100%', width: '18rem' }}>
                            <img 
                                style={{height: '100%', width: '100%', objectFit: 'cover'}}
                                src={product.image_link} 
                                className="card-img-top" 
                                alt={product.name} 
                            />
                            <div className="card-body-style card-body text-center">
                                <h5 className="card-title">{product.name}</h5>
                                <p className="card-text">{product.description}</p>
                            </div>
                        </div>
                    </div>
                ))}
            </div>
        </div>

        </Container>
  )
}

export default TopSellingSection
