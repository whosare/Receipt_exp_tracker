import React from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import Navbar from './components/Navbar';
import Login from './components/Login';
import Register from './components/Register';
import UploadReceipt from './components/UploadReceipt';
import ExpenseList from './components/ExpenseList';

function App() {
  return (
    <>
      <Navbar />
      <Routes>
        <Route path="/" element={<Navigate to="/login" />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/upload" element={<UploadReceipt />} />
        <Route path="/expenses" element={<ExpenseList />} />
        <Route path="*" element={<div className="text-red-600 text-center">Page Not Found</div>} />
      </Routes>
    </>
  );
}

export default App;
