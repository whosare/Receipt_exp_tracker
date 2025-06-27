// components/Navbar.jsx
import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => (
  <nav style={{ padding: "10px", borderBottom: "1px solid gray" }}>
    <Link to="/upload" style={{ marginRight: "10px" }}>Upload Receipt</Link>
    <Link to="/expenses" style={{ marginRight: "10px" }}>Expenses</Link>
    <Link to="/login">Logout</Link>
  </nav>
  
);


export default Navbar;
