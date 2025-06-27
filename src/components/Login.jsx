import React, { useState } from 'react';
import { loginUser } from '../services/api';

function LoginForm({ onLoginSuccess }) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await loginUser({ username: email, password });
      localStorage.setItem('token', response.data.access_token);
      setMessage('Login successful.');
      onLoginSuccess(); // callback to update parent state
    } catch (err) {
      console.error(err);
      setMessage('Login failed. Check your credentials.');
    }
  };
  return ( //addded
    <div className="text-2xl text-center text-green-600 mt-20">Register Page</div>
  );
  return (
    <form onSubmit={handleLogin}>
      <h2>Login</h2>
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
      <button type="submit">Login</button>
      {message && <p>{message}</p>}
    </form>
  );
}



export default LoginForm;
