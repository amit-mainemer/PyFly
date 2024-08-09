import React, { useState } from "react";
import css from "./LoginForm.module.css";
import {
  Box,
  TextField,
  Button,
  Typography,
  Alert,
  FormControl,
  InputLabel,
  OutlinedInput,
  InputAdornment,
  IconButton,
} from "@mui/material";
import AirplanemodeActiveIcon from "@mui/icons-material/AirplanemodeActive";
import VisibilityOff from "@mui/icons-material/VisibilityOff";
import Visibility from "@mui/icons-material/Visibility";
import { api } from "../../api";
import { useAuth } from "../../AuthContext";
import { useNavigate } from "react-router-dom";

export const LoginForm = () => {
  const [id, setId] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();
  const { login } = useAuth();

  const handleClickShowPassword = () => setShowPassword((show) => !show);

  const handleMouseDownPassword = (event) => {
    event.preventDefault();
  };

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
          <AirplanemodeActiveIcon color="primary" />
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
        <FormControl variant="outlined">
          <InputLabel htmlFor="outlined-adornment-password" size="small">
            Password
          </InputLabel>
          <OutlinedInput
            id="outlined-adornment-password"
            type={showPassword ? "text" : "password"}
            size="small"
            onChange={(e) => setPassword(e.target.value)}
            endAdornment={
              <InputAdornment position="end">
                <IconButton
                  aria-label="toggle password visibility"
                  onClick={handleClickShowPassword}
                  onMouseDown={handleMouseDownPassword}
                  edge="end"
                >
                  {showPassword ? <VisibilityOff /> : <Visibility />}
                </IconButton>
              </InputAdornment>
            }
            label="Password"
          />
        </FormControl>
        <Box display={"flex"} justifyContent={"space-between"} gap={2} alignItems={"center"}>
          <Typography
            className={css.caption}
            variant="caption"
            onClick={() => navigate("/signup")}
          >
            Don't have an account?
          </Typography>

          <Button
            variant="contained"
            style={{ width: "40%", marginLeft: "auto" }}
            onClick={() => submit()}
          >
            Login
          </Button>
        </Box>
        <Box>
          {error && (
            <Alert severity="error" style={{ fontSize: "12px" }}>
              {error}
            </Alert>
          )}
        </Box>
      </Box>
    </Box>
  );
};
