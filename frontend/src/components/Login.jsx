import React, { useState } from 'react';
import { useAuth } from '../context/AuthContext';

const Login = ({ onToggleAuth }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const { login } = useAuth();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    const success = await login(username, password);
    if (!success) setError('Invalid username or password');
  };

  return (
    <div className="card auth-card">
      <h2>Login to Quiz App</h2>
      <form onSubmit={handleSubmit} className="auth-form">
        <div className="form-group">
          <label>Username</label>
          <input 
            type="text" 
            value={username} 
            onChange={(e) => setUsername(e.target.value)} 
            required 
          />
        </div>
        <div className="form-group">
          <label>Password</label>
          <input 
            type="password" 
            value={password} 
            onChange={(e) => setPassword(e.target.value)} 
            required 
          />
        </div>
        {error && <p className="error-text">{error}</p>}
        <button type="submit" className="btn btn-primary">Login</button>
      </form>
      <p style={{ marginTop: '1rem' }}>
        Don't have an account? <span className="auth-link" onClick={onToggleAuth}>Sign Up</span>
      </p>
    </div>
  );
};

export default Login;
