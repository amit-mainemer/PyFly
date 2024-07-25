// src/routes/Routes.tsx
import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { routes } from "./routes";
import { Navbar } from "./components/Navbar/Navbar";
import { ProtectedRoute } from "./components/ProtectedRoute";
import { AuthProvider } from "./AuthContext";

export const AppRouter = () => (
  <Router>
    <AuthProvider>
      <Navbar />
      <Routes>
        {routes.map(({ link, Component, isProtected = false }) =>
          isProtected ? (
            <Route key={link} element={<ProtectedRoute />}>
              <Route path={link} element={<Component />} />
            </Route>
          ) : (
            <Route key={link} path={link} element={<Component />} />
          )
        )}
      </Routes>
    </AuthProvider>
  </Router>
);
