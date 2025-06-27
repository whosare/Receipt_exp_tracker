import React, { useState } from 'react';
import { registerUser } from '../services/api';

function RegisterForm({ onRegisterSuccess }) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');

  const handleRegister = async (e) => {
    e.preventDefault();
    try {
      await registerUser({ email, password });
      setMessage('Registration successful. Please log in.');
      onRegisterSuccess(); // optional callback
    } catch (err) {
      console.error(err);
      setMessage('Registration failed. Try another email.');
    }
  };
  return (
    <div className="text-2xl text-center text-green-600 mt-20">Register Page</div>
  );
  return (
    <form onSubmit={handleRegister}>
      <h2>Register</h2>
      <input
        type="email"
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        required
      /><br />
      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        required
      /><br />
      <button type="submit">Register</button>
      {message && <p>{message}</p>}
    </form>
  );
}



export default RegisterForm;
