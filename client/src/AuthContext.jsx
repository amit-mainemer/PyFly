import React, { createContext, useEffect, useContext, useState } from "react";
import { jwtDecode } from "jwt-decode";

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [auth, setAuth] = useState(null);
  const [user, setUser] = useState(null);

  const token = localStorage.getItem("access_token");

  useEffect(() => {
    setAuth(!!token);
    setUser(decodeToken(token)?.sub);
  }, [token]);

  const decodeToken = (token) => {
    try {
      return jwtDecode(token);
    } catch (error) {
      return null;
    }
  };

  const login = (token) => {
    localStorage.setItem("access_token", token);
    setAuth(true);
  };

  const logout = () => {
    localStorage.removeItem("access_token");
    setAuth(false);
  };

  return (
    <AuthContext.Provider value={{ auth, login, logout, user }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
