import React, { createContext, useContext, useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [auth, setAuth] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    // Check if there is a token in localStorage
    const token = localStorage.getItem("access_token");
    if (token) {
      setAuth(true);
    } else {
      setAuth(false);
      navigate("/login");
    }
  }, [navigate]);

  const login = (token) => {
    localStorage.setItem("access_token", token);
    setAuth(true);
    navigate("/");
  };

  const logout = () => {
    localStorage.removeItem("access_token");
    setAuth(false);
    navigate("/login"); 
  };

  return (
    <AuthContext.Provider value={{ auth, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
