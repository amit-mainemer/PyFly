import React from "react";
import { Box } from "@mui/material";
import { SignUpForm } from "../components/SignUpForm/SignUpForm";
import { Navigate  } from "react-router-dom";
import { useAuth } from "../AuthContext";

export const SignUp = () => {
  const { auth } = useAuth();

  if (auth) {
    return <Navigate to="/" />;
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
      <SignUpForm />
    </Box>
  );
};
