import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import MainLayout from './layout/MainLayout.jsx';
import HomePage from './pages/HomePage.jsx';
import LoginPage from './pages/LoginPage.jsx';
import RegisterPage from './pages/RegisterPage.jsx';
import ProductDetailsPage from './pages/ProductDetailsPage.jsx';
import ProductGalleryPage from './pages/ProductGalleryPage.jsx';
import CartPage from './pages/CartPage.jsx';
import OrderSuccessPage from './pages/OrderSuccessPage.jsx';


import { CartProvider } from './context/cartContext';

function App() {
  return (
   
    <CartProvider>
      <Router>
        <Routes>
          {/* <Route path="/" element={<RegisterPage />} /> // fisrt page */}
          <Route path="/" element={<MainLayout />} />
          <Route path="/home" element={<HomePage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/register" element={<RegisterPage />} />
          <Route path="/gallery" element={<ProductGalleryPage />} />
          <Route path="/products/:id" element={<ProductDetailsPage />} />
          <Route path="/cart" element={<CartPage />} />
          <Route path="/order-success" element={<OrderSuccessPage />} />
        </Routes>
      </Router>
    </CartProvider>
  );
}

export default App;
