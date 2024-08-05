// src/routes/Routes.tsx
import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { routes } from "./routes";
import { Navbar } from "./components/Navbar/Navbar";
import { Box } from "@mui/material";
import { ProtectedRoute } from "./components/ProtectedRoute";

export const AppRouter = () => (
  <Router>
    <Navbar />
    <Box
      style={{
        position: "relative",
        height: "calc(100vh - 48px)",
        overflowY: "scroll",
      }}
    >
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
    </Box>
  </Router>
);
