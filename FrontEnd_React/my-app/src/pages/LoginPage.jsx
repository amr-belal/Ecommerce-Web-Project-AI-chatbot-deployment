import React, { useState } from 'react'
import '../style/Login.css'
import '../style/register.css'
import LightRays from '../style/RegistreAnimations.jsx';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
function LoginPage() {
   const [formData, setFormData] = useState({
    email: '',
    password: ''
  });
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
   
      const res = await axios.get(`http://localhost:3005/users?email=${formData.email}`);
      
      if (res.data.length === 0) {
        setError(" Email not found!");
        return;
      }

      const user = res.data[0];

       
      if (user.password !== formData.password) {
        setError(" Incorrect password!");
        return;
      }

      navigate('/home');

    } catch (err) {
      console.error("Login error:", err);
      setError(" Something went wrong!");
    }
  };

  return (
    <>

    <div style={{ 
        position: 'fixed', 
        top: 0, 
        left: 0, 
        width: '100vw', 
        height: '100vh', 
        zIndex: 1 
      }}>
      <LightRays
    raysOrigin="top-center"
    raysColor="#F5AB98"
    raysSpeed={1.2}
    lightSpread={0.6}
    rayLength={1.5}
    followMouse={true}
    mouseInfluence={0.15}
    noiseAmount={0.05}
    distortion={0.08}
    className="custom-rays"
/>


    </div>



        <div className="container-register">
    <div className='form-container'>
        <h2>Log In</h2>
        <form onSubmit={handleLogin}>
            <div className="mb-3">
                <label htmlFor="exampleInputEmail1" className="form-label">Email address</label>
                <input 
                    type="email" 
                    className="form-control" 
                    id="email" 
                    name="email" 
                    value={formData.email} 
                    onChange={handleChange} 
                    required 
                  />
                <div id="emailHelp" className="form-text">We'll never share your email with anyone else.</div>
            </div>
           
            <div className="mb-3">
                <label htmlFor="exampleInputPassword1" className="form-label">Password</label>
                <input 
                      type="password" 
                      className="form-control" 
                      id="password" 
                      name="password" 
                      value={formData.password} 
                      onChange={handleChange} 
                      required 
                    />
                
            </div>
           
            <button type="submit" className="btn btn-primary">Log in</button>
        </form>
    </div>
</div>
            

    </>

)
}

export default LoginPage
