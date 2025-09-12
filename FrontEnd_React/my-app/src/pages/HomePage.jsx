import React from 'react'
import Header from '../components/Header'
import HeroSection from '../components/HeroSection'
import TopSellingSection from '../components/TopSellingSection'
import ProductDetailsPage from './ProductDetailsPage'
import ProductGallery from './ProductGalleryPage'
import Footer from '../components/Footer'
import Newsletter from '../components/NewsLetter'
import ChatBot from '../components/ChatBot'
import ScrollToTop from '../components/ScrollToTop'
import NewCollectionSlider from '../components/ProductSlider'
import ProductSlider from '../components/ProductSlider';
function HomePage() {
  return (
     <div>
      <Header/>
      
      <HeroSection/>
      
      <TopSellingSection/>
      <ProductSlider type="new"/> 

      {/* <ProductDetailsPage/> */}
      <ProductGallery/>
      <Newsletter/>
      <Footer/>
      <ScrollToTop/>
      <ChatBot/>
    </div>
     
  )
}

export default HomePage
