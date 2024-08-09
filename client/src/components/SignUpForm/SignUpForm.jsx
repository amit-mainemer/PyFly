import React, { useState } from "react";
import css from "./SignUpForm.module.css";
import {
  Box,
  TextField,
  Button,
  Alert,
  Typography,
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
import { useNavigate } from "react-router-dom";

export const SignUpForm = () => {
  const [name, setName] = useState("");
  const [id, setId] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const navigate = useNavigate();

  const handleClickShowPassword = () => setShowPassword((show) => !show);

  const handleMouseDownPassword = (event) => {
    event.preventDefault();
  };

  const submit = async () => {
    setError("")
    try {
      await api.post("/users", {
        full_name: name,
        real_id: parseInt(id),
        password,
      });
      navigate("/login");
    } catch (ex) {
      console.warn(ex);

      let errorString = ""
      Object.entries(ex.response.data.messages).forEach(([key, value]) => {
        errorString += `${key}: ${value} <br />`
      })
      setError(errorString)
    }
  };

  return (
    <Box className={css.container}>
      <Box className={css.formContainer}>
        <Box className={css.title}>
          <AirplanemodeActiveIcon color="primary" />
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
        <Box
          style={{
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
          }}
        >
          <Typography
            className={css.caption}
            variant="caption"
            onClick={() => navigate("/login")}
          >
            already registered?
          </Typography>
          <Button variant="contained" style={{ width: "40%" }} onClick={submit}>
            SignUp
          </Button>
        </Box>
        <Box>
          {error && <Alert severity="error" style={{ fontSize: "12px", maxWidth: "292px" }}  ><span dangerouslySetInnerHTML={{__html: error}}></span> </Alert>}
        </Box>
      </Box>
    </Box>
  );
};
