import React, { useState } from 'react'
import '../style/register.css'
import LightRays from '../style/RegistreAnimations.jsx';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

function RegisterPage() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    password: '',
  });

  const [errors, setErrors] = useState({});
  const navigate = useNavigate();

  // ✅ validation function
  const validateForm = () => {
    let newErrors = {};

    if (!formData.name.trim()) {
      newErrors.name = "Name is required";
    } else if (formData.name.length < 3) {
      newErrors.name = "Name must be at least 3 characters";
    }

    if (!formData.email) {
      newErrors.email = "Email is required";
    } else if (!/\S+@\S+\.\S+/.test(formData.email)) {
      newErrors.email = "Email is invalid";
    }

    if (!formData.password) {
      newErrors.password = "Password is required";
    } else if (formData.password.length < 6) {
      newErrors.password = "Password must be at least 6 characters";
    }

    setErrors(newErrors);

    // لو مفيش errors هنرجع true
    return Object.keys(newErrors).length === 0;
  };

  const submit = async (e) => {
    e.preventDefault();

    if (!validateForm()) {
      return; // لو فيه errors متبعتش request
    }

    try {
      const res = await axios.post("http://localhost:3005/users", formData);
      console.log(" Server Response:", res.data);
      navigate('/home');
    } catch (err) {
      console.error("Error submitting form:", err);
    }
  };

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
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
          <h2>Create Account</h2>
          <form onSubmit={submit}>
            <div className="mb-3">
              <label htmlFor="name" className="form-label">User Name</label>
              <input
                type="text"
                className={`form-control ${errors.name ? 'is-invalid' : ''}`}
                id="name"
                name="name"
                value={formData.name}
                onChange={handleChange}
              />
              {errors.name && <div className="invalid-feedback">{errors.name}</div>}
              <div className="form-text">Enter your Fullname.</div>
            </div>

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
              <div className="form-text">We'll never share your email with anyone else.</div>
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

            <div className="mb-3 form-check">
              <input type="checkbox" className="form-check-input" id="exampleCheck1" required />
              <label className="form-check-label" htmlFor="exampleCheck1">I agree to the terms</label>
            </div>

            <button type="submit" className="btn btn-primary">Register</button>
          </form>
        </div>
      </div>
    </>
  )
}

export default RegisterPage;



// import React, { useState } from 'react'
// import '../style/register.css'
// import LightRays from '../style/RegistreAnimations.jsx';
// import { useNavigate } from 'react-router-dom';
// import axios from 'axios';
// function RegisterPage() {

//     const [formData, setFormData] = useState({
        
//         name: '',
//         email: '',
//         password: '',
//       });
//       const [errors, setErrors] = useState({});
    
//         const navigate = useNavigate();
//           const submit = async (e)=>{
//         e.preventDefault();
//         const res =await axios.post("http://localhost:3005/users", formData);

//          console.log(" Server Response:", res.data);

 

//         navigate('/home');

    
//     }

    

//     const handleChange = (e) => {
//         setFormData({
//             ...formData,
//             [e.target.name]: e.target.value
//         })
//     }


//  return (
//     <>
//       <div style={{ 
//         position: 'fixed', 
//         top: 0, 
//         left: 0, 
//         width: '100vw', 
//         height: '100vh', 
//         zIndex: 1 
//       }}>
//         <LightRays
//           raysOrigin="top-center"
//           raysColor="#F5AB98"
//           raysSpeed={1.2}
//           lightSpread={0.6}
//           rayLength={1.5}
//           followMouse={true}
//           mouseInfluence={0.15}
//           noiseAmount={0.05}
//           distortion={0.08}
//           className="custom-rays"
//         />
//       </div>

//       <div className="container-register">
//         <div className='form-container'>
//           <h2>Create Account</h2> 
//           <form onSubmit={submit}>
//             <div className="mb-3">
//               <label htmlFor="name" className="form-label">User Name</label>
//               <input 
//                 type="text" 
//                 className="form-control" 
//                 id="name" 
//                 name="name"
//                 value={formData.name}
//                 onChange={handleChange}
//                 required
//               />
//               <div className="form-text">Enter your Fullname.</div>
//             </div>

//             <div className="mb-3">
//               <label htmlFor="email" className="form-label">Email address</label>
//               <input 
//                 type="email" 
//                 className="form-control" 
//                 id="email" 
//                 name="email"
//                 value={formData.email}
//                 onChange={handleChange}
//                 required
//               />
//               <div className="form-text">We'll never share your email with anyone else.</div>
//             </div>

//             <div className="mb-3">
//               <label htmlFor="password" className="form-label">Password</label>
//               <input 
//                 type="password" 
//                 className="form-control" 
//                 id="password" 
//                 name="password"
//                 value={formData.password}
//                 onChange={handleChange}
//                 required
//               />
//             </div>

//             <div className="mb-3 form-check">
//               <input type="checkbox" className="form-check-input" id="exampleCheck1" required />
//               <label className="form-check-label" htmlFor="exampleCheck1">I agree to the terms</label>
//             </div>

//             <button type="submit" className="btn btn-primary">Register</button>
//           </form>
//         </div>
//       </div>
//     </>
//   )
// }

// export default RegisterPage
