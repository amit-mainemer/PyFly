import React, { useEffect } from "react";
import { Box } from "@mui/material";
import { SignUpForm } from "../components/SignUpForm/SignUpForm";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../AuthContext";

export const SignUp = () => {
  const navigate = useNavigate();
  const { auth } = useAuth();
  useEffect(() => {
    if (auth) {
      navigate("/");
    }
  }, [auth]);

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
