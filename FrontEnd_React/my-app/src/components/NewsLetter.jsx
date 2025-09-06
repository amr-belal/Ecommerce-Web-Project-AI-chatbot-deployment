import React, { useState } from 'react';
import '../style/Newsletter.css';

const Newsletter = () => {
  const [email, setEmail] = useState('');

  const handleSubmit = () => {
    if (email) {
      console.log('Subscribed with email:', email);
      // Handle subscription logic here
      setEmail('');
    }
  };

  return (
    <section className="newsletter-section">
      <div className="container">
        <div className="row justify-content-center">
          <div className="col-lg-8 col-md-10">
            <div className="newsletter-content text-center">
              <h2 className="newsletter-title">
                Stay Updated: Subscribe for<br />
                Exclusive Content
              </h2>
              <p className="newsletter-subtitle">
                Subscribe Now: Get Exclusive Updates and Content!
              </p>
              
              <div className="newsletter-form">
                <div className="input-group">
                  <input
                    type="email"
                    className="form-control newsletter-input"
                    placeholder="Enter your email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                  />
                  <button onClick={handleSubmit} className="btn newsletter-btn">
                    Subscribe Now
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Newsletter;