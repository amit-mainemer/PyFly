import React, { createContext, useEffect, useContext, useState } from "react";
import { logMessage } from "./api";
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
      console.error("Invalid token:", error);
      return null;
    }
  };

  const login = (token) => {
    localStorage.setItem("access_token", token);
    setAuth(true);
    window.location.href = "/";
    const userInfo = decodeToken(token);
    logMessage("User logged in. id: " + userInfo.id);
  };

  const logout = () => {
    localStorage.removeItem("access_token");
    setAuth(false);
    const userInfo = decodeToken(token);
    window.location.href = "/login";
    logMessage("User logged out. id: " + userInfo.id);
  };

  return (
    <AuthContext.Provider value={{ auth, login, logout, user }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
