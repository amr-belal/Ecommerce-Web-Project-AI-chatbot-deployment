import React from 'react';
import '../style/footer.css';

const Footer = () => {
  return (
    <footer className="custom-footer">
      <div className="container">
        <div className="row">
          <div className="col-md-3">
            <h5 className="footer-brand">Rouh</h5>
          </div>
          
          <div className="col-md-2">
            <h6 className="footer-title">Action</h6>
            <ul className="footer-links">
              <li><a href="#" className="footer-link">About us</a></li>
              <li><a href="#" className="footer-link">Contact us</a></li>
              <li><a href="#" className="footer-link">Our Team</a></li>
            </ul>
          </div>
          
          <div className="col-md-3">
            <h6 className="footer-title">Support</h6>
            <ul className="footer-links">
              <li><a href="#" className="footer-link">Shopping and returns</a></li>
              <li><a href="#" className="footer-link">Legal and privacy</a></li>
              <li><a href="#" className="footer-link">Track and order</a></li>
            </ul>
          </div>
          
          <div className="col-md-4 text-end">
            <div className="social-buttons">
              <button className="btn social-btn">Instagram</button>
              <button className="btn social-btn">Pinterest</button>
            </div>
          </div>
        </div>
        
        <hr className="footer-divider" />
        
        <div className="row">
          <div className="col-12 text-center">
            <p className="footer-copyright">
              Rouh © 2023–2024 All rights reserved.
            </p>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;