import React, { useState } from "react";
import css from "./SignUpForm.module.css";
import { Box, TextField, Button, Typography } from "@mui/material";
import AirplanemodeActiveIcon from "@mui/icons-material/AirplanemodeActive";
import { api } from "../../api";
import { useNavigate } from "react-router-dom";

export const SignUpForm = () => {
  const [name, setName] = useState("");
  const [id, setId] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();


  const submit = async () => {
    try {
      await api.post("/users", {
        full_name: name,
        real_id: parseInt(id),
        password,
      });
      navigate("/login");
    } catch (ex) {
      console.warn(ex);
    }
  };

  return (
    <Box className={css.container}>
      <Box className={css.formContainer}>
        <Box className={css.title}>
          <AirplanemodeActiveIcon />
          <Typography variant="h6">Register to PyFly</Typography>
        </Box>
        <TextField
          label="Full Name"
          size="small"
          value={name}
          onChange={(e) => setName(e.target.value)}
          variant="outlined"
        />
        <TextField
          label="ID Number"
          size="small"
          value={id}
          type="number"
          onChange={(e) => setId(e.target.value)}
          variant="outlined"
        />
        <TextField
          label="Password"
          size="small"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          variant="outlined"
          type="password"
        />
        <Box style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
          <Typography className={css.caption} variant="caption" onClick={() => navigate("/login")}>already registered?</Typography>
          <Button
            variant="contained"
            style={{ width: "40%"}}
            onClick={submit}
          >
            SignUp
          </Button>
        </Box>
      </Box>
    </Box>
  );
};
