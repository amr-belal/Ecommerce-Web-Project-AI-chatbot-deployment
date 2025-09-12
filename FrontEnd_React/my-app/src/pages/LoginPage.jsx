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

  const [errors, setErrors] = useState({});
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  // ✅ validate form inputs
  const validateForm = () => {
    let newErrors = {};

    if (!formData.email) {
      newErrors.email = "Email is required";
    } else if (!/\S+@\S+\.\S+/.test(formData.email)) {
      newErrors.email = "Email format is invalid";
    }

    if (!formData.password) {
      newErrors.password = "Password is required";
    } else if (formData.password.length < 6) {
      newErrors.password = "Password must be at least 6 characters";
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleLogin = async (e) => {
    e.preventDefault();

    if (!validateForm()) return;

    try {
      const res = await axios.get(`http://localhost:3005/users?email=${formData.email}`);
      
      if (res.data.length === 0) {
        // ❌ الإيميل مش موجود
        setErrors({ email: "Email not found!" });
        return;
      }

      const user = res.data[0];

      if (user.password !== formData.password) {
        // ❌ الباسورد غلط
        setErrors({ password: "Incorrect password!" });
        return;
      }

      // ✅ تسجيل الدخول ناجح
      navigate('/home');
    } catch (err) {
      console.error("Login error:", err);
      setErrors({ email: "Something went wrong, please try again!" });
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
              <label htmlFor="email" className="form-label">Email address</label>
              <input 
                type="email" 
                className={`form-control ${errors.email ? 'is-invalid' : ''}`} 
                id="email" 
                name="email" 
                value={formData.email} 
                onChange={handleChange} 
              />
              {errors.email && <div className="invalid-feedback">{errors.email}</div>}
              <div id="emailHelp" className="form-text">We'll never share your email with anyone else.</div>
            </div>
           
            <div className="mb-3">
              <label htmlFor="password" className="form-label">Password</label>
              <input 
                type="password" 
                className={`form-control ${errors.password ? 'is-invalid' : ''}`} 
                id="password" 
                name="password" 
                value={formData.password} 
                onChange={handleChange} 
              />
              {errors.password && <div className="invalid-feedback">{errors.password}</div>}
            </div>
           
            <button type="submit" className="btn btn-primary">Log in</button>
          </form>
        </div>
      </div>
    </>
  )
}

export default LoginPage;
