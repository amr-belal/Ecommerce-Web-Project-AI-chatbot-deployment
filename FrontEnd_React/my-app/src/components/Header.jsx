import React from 'react'
import { Navbar, Nav, Container } from "react-bootstrap";
import '../style/Header.css'
import { useNavigate } from 'react-router-dom';
import { Link } from "react-router-dom";
function Header() {

  
    
        const navigate = useNavigate();
          const submit =(e)=>{
        e.preventDefault();
        navigate('/home');
    
    }
  return (
  
<>
  <Navbar expand="lg" className="main-navbar">
    <Container>
    
      <Navbar.Toggle aria-controls="main-navbar-nav" />
      <Navbar.Collapse id="main-navbar-nav" className="justify-content-between">

     
        <Nav className="ms-3 d-flex align-items-center">
          <Nav.Link href="#">
            <i className="bi bi-bag fs-5"></i>
          </Nav.Link>
        </Nav>

        <Nav className="mx-auto">
          <Nav.Link href="#home" className="mx-3" id="component">
            Home
          </Nav.Link>
          <Nav.Link href="#features" className="mx-3" id="component">
            Collections
          </Nav.Link>

          <Navbar.Brand href="#home" className="mx-3" id="brand">
            Rouh
          </Navbar.Brand>


          <Nav.Link href="#features" className="mx-3" id="component">
            Men
          </Nav.Link>
          <Nav.Link href="#pricing" className="mx-3" id="component">
            Women
          </Nav.Link>
        </Nav>

      
        <Nav className="me-3 d-flex align-items-center">
          <Nav.Link as={Link} to="/register">
            <i className="bi bi-person-add fs-5"></i>
          </Nav.Link>
          <Nav.Link as={Link} to="/login">
            <i className="bi bi-person fs-5"></i>
          </Nav.Link>
        </Nav>
      </Navbar.Collapse>
    </Container>
  </Navbar>
</>

  )
}

export default Header
