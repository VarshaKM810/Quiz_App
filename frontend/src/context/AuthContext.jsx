import React, { createContext, useState, useContext, useEffect, useCallback } from 'react';
import axios from 'axios';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const safeGetItem = (key) => {
    try { return localStorage.getItem(key); }
    catch (e) { return null; }
  };
  const safeSetItem = (key, value) => {
    try { localStorage.setItem(key, value); }
    catch (e) {}
  };
  const safeRemoveItem = (key) => {
    try { localStorage.removeItem(key); }
    catch (e) {}
  };

  const [user, setUser] = useState(null);
  const [token, setToken] = useState(() => safeGetItem('token'));
  const [loading, setLoading] = useState(true);

  const logout = useCallback(() => {
    setToken(null);
  }, []);

  useEffect(() => {
    let interceptorId = null;

    if (token) {
      safeSetItem('token', token);
      axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;

      // Intercept 401 errors to auto-logout
      interceptorId = axios.interceptors.response.use(
        (response) => response,
        (error) => {
          if (error.response?.status === 401) {
            // Only logout if it's not the login/signup endpoint
            const url = error.config?.url || '';
            if (!url.includes('/api/token') && !url.includes('/api/signup')) {
              logout();
            }
          }
          return Promise.reject(error);
        }
      );

      // Fetch real username from profile
      axios.get('http://localhost:8000/api/user/profile')
        .then(res => setUser({ username: res.data.username, xp: res.data.xp, level: res.data.level }))
        .catch(() => {
          // Token is invalid/expired — force logout
          logout();
        })
        .finally(() => setLoading(false));

    } else {
      safeRemoveItem('token');
      delete axios.defaults.headers.common['Authorization'];
      setUser(null);
      setLoading(false);
    }

    return () => {
      if (interceptorId !== null) {
        axios.interceptors.response.eject(interceptorId);
      }
    };
  }, [token, logout]);

  const login = async (username, password) => {
    try {
      const response = await axios.post('http://localhost:8000/api/token', { username, password });
      setToken(response.data.access_token);
      return true;
    } catch (error) {
      console.error('Login failed', error);
      return false;
    }
  };

  const signup = async (username, email, password) => {
    try {
      await axios.post('http://localhost:8000/api/signup', { username, email, password });
      return await login(username, password);
    } catch (error) {
      console.error('Signup failed', error);
      return false;
    }
  };

  return (
    <AuthContext.Provider value={{ user, token, login, signup, logout, loading }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
