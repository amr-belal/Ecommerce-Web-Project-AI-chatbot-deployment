import React from 'react';
import '../style/HeroSection.css';

function HeroSection() {
  return (
    <section className="hero-section position-relative overflow-hidden">
      <div className="container-fluid h-100 position-relative">

         {/* Happy Customers Badge - Desktop */}
        <div className="customers-badge-desktop d-none d-lg-flex position-absolute">
          <div className="customer-avatars-desktop d-flex me-3">
            <div className="avatar-1"></div>
            <div className="avatar-2"></div>
          </div>
          <p className="customer-text-desktop mb-0">Happy<br/>Customers</p>
        </div>

        {/* Mobile Happy Customers Badge */}
        <div className="customers-badge-mobile d-flex d-lg-none justify-content-center mb-3 pt-4">
          <div className="customers-content-mobile d-flex align-items-center">
            <div className="customer-avatars-mobile d-flex me-2">
              <div className="avatar-mobile-1"></div>
              <div className="avatar-mobile-2"></div>
            </div>
            <p className="customer-text-mobile mb-0 small fw-semibold text-dark">Happy Customers</p>
          </div>
        </div>

      
          {/* <div className="organic-badge">
          <h5 className="mb-0">Our Unique<br/>Product 100%<br/>Organic</h5>
        </div> */}
        <div className="organic-badge-desktop d-none d-lg-flex position-absolute">
          <h5 className="organic-text-desktop">Our Unique<br/>Product 100%<br/>Organic</h5>
        </div>

        {/* Mobile Organic Badge */}
        <div className="organic-badge-mobile d-flex d-lg-none justify-content-center mb-3">
          <div className="organic-content-mobile text-center">
            <h6 className="organic-text-mobile mb-0 fw-semibold">Our Unique Product 100% Organic</h6>
          </div>
        </div>


        
             <div className="play-button"></div> <div className="play-button-desktop d-none d-lg-flex position-absolute">
          <div className="play-icon"></div>
        </div>
  

        <div className="perfume-left-desktop d-none d-lg-block position-absolute">
          <img 
            src="https://images.unsplash.com/photo-1701291927826-c7775869d822?q=80&w=710&auto=format&fit=crop" 
            alt="Perfume left"
            className="perfume-img-desktop"
          />
        </div>

        {/* Right Perfume Image - Desktop */}
        <div className="perfume-right-desktop d-none d-lg-block position-absolute">
          <img 
            src="https://images.unsplash.com/photo-1547887537-6158d64c35b3?q=80&w=687&auto=format&fit=crop" 
            alt="Perfume right"
            className="perfume-img-desktop"
          />
        </div>
       

        <div className="row d-lg-none mb-4">
          <div className="col-6">
            <div className="perfume-mobile-container mx-auto">
              <img 
                src="https://images.unsplash.com/photo-1701291927826-c7775869d822?q=80&w=710&auto=format&fit=crop" 
                alt="Perfume left"
                className="perfume-img-mobile"
              />
            </div>
          </div>
          <div className="col-6">
            <div className="perfume-mobile-container mx-auto">
              <img 
                src="https://images.unsplash.com/photo-1547887537-6158d64c35b3?q=80&w=687&auto=format&fit=crop" 
                alt="Perfume right"
                className="perfume-img-mobile"
              />
            </div>
          </div>
        </div>

        {/* Content */}
        <div className="hero-content-responsive text-center">
          <h1 className="main-title-responsive">
            Best Perfume<br/>Collection for You
          </h1>
          <p className="subtitle-responsive">
            Discover the Best Perfume Collection: Find Your Signature Scent Today
          </p>
          <button className="buy-now-btn-responsive">Buy Now</button>
        </div>

        {/* Essence Text - Desktop */}
        <div className="essence-text-desktop d-none d-lg-block position-absolute">essence unleashed</div>

        {/* Mobile Essence Text */}
        <div className="essence-text-mobile d-lg-none text-center mb-3">essence unleashed</div>

        {/* Essence Description - Desktop */}
        <div className="essence-description-desktop d-none d-lg-block position-absolute text-center">
          <h4 className="essence-title-desktop">Unleash Your</h4>
          <p className="essence-subtitle-desktop">Essence with the<br/>Every Spritz.</p>
        </div>

        {/* Mobile Essence Description */}
        <div className="essence-description-mobile d-lg-none text-center mb-4">
          <h4 className="essence-title-mobile">Unleash Your</h4>
          <p className="essence-subtitle-mobile">Essence with the Every Spritz.</p>
        </div>

        {/* Learn More - Desktop */}
        <div className="learn-more-desktop d-none d-lg-block position-absolute">
          <a href="#" className="learn-more-link">Learn More ↗</a>
        </div>

        {/* Mobile Learn More */}
        <div className="learn-more-mobile d-lg-none text-center mb-4">
          <a href="#" className="learn-more-link">Learn More ↗</a>
        </div>

        {/* Scroll Indicator - Desktop */}
        <div className="scroll-indicator-desktop d-none d-lg-block position-absolute" 
             onClick={() => window.scrollTo({ top: window.innerHeight, behavior: 'smooth' })}>
          <div className="scroll-down-desktop">
            <div className="scroll-arrow"></div>
          </div>
        </div>

        {/* Mobile Scroll Indicator */}
        <div className="scroll-indicator-mobile d-lg-none text-center">
          <div className="scroll-down-mobile mx-auto" 
               onClick={() => window.scrollTo({ top: window.innerHeight, behavior: 'smooth' })}>
            <div className="scroll-arrow"></div>
          </div>
        </div>

      </div>
    </section>
  );
}

export default HeroSection;
