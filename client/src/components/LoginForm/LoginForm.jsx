import React, { useState } from "react";
import css from "./LoginForm.module.css";
import { Box, TextField, Button, Typography, Alert } from "@mui/material";
import AirplanemodeActiveIcon from "@mui/icons-material/AirplanemodeActive";
import { api } from "../../api";
import { useAuth } from "../../AuthContext";

export const LoginForm = () => {
  const [id, setId] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const { login } = useAuth();

  const submit = async () => {
    try {
      const response = await api.post("/login", {
        real_id: parseInt(id),
        password,
      });
      login(response.data.access_token);
    } catch (ex) {
      console.warn(ex.response.status);
      setError("Wrong Credentials");
    }
  };

  return (
    <Box className={css.container}>
      <Box className={css.formContainer}>
        <Box className={css.title}>
          <AirplanemodeActiveIcon />
          <Typography variant="h6">Welcome to PyFly</Typography>
        </Box>
        <TextField
          label="ID Number"
          size="small"
          value={id}
          type="number"
          onChange={(e) => setId(e.target.value)}
          variant="outlined"
          autoComplete="id"
        />
        <TextField
          label="Password"
          size="small"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          variant="outlined"
          type="password"
        />
        <Box display={"flex"} justifyContent={"space-between"} gap={2}>
          {error && (
            <Alert severity="error" style={{ fontSize: "12px" }}>
              {error}
            </Alert>
          )}

          <Button
            variant="contained"
            style={{ width: "40%", marginLeft: "auto" }}
            onClick={() => submit()}
          >
            Login
          </Button>
        </Box>
      </Box>
    </Box>
  );
};
