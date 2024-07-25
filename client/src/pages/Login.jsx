import React from "react";
import { Box } from "@mui/material";
import { LoginForm } from "../components/LoginForm/LoginForm";
import {  Navigate } from "react-router-dom";
import { useAuth } from "../AuthContext";

export const Login = () => {
  const { auth } = useAuth();
  if(auth) {
    return <Navigate to="/" />
  }
  return (
    <Box
      style={{
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        height: "calc(100% - 60px)",
      }}
    >
      <LoginForm />
    </Box>
  );
};
