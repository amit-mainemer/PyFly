import React from "react";
import css from "./Navbar.module.css";
import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import Toolbar from "@mui/material/Toolbar";
import FlightTakeoffIcon from "@mui/icons-material/FlightTakeoff";
import Logout from "@mui/icons-material/Logout";
import IconButton from "@mui/material/IconButton";
import Tooltip from "@mui/material/Tooltip";
import Button from "@mui/material/Button";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../../AuthContext";

export const Navbar = () => {
  const navigate = useNavigate();
  const { auth, user, logout } = useAuth();

  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar
        position="static"
        className={css.NavbarBackground}
        color="inherit"
      >
        <Toolbar variant="dense">
          <IconButton color="inherit">
            <FlightTakeoffIcon />
          </IconButton>
          {auth ? (
            <>
              <Button onClick={() => navigate("/")} color="inherit">
                Flights
              </Button>
              <Button onClick={() => navigate("/profile")} color="inherit">
                My Profile
              </Button>
            </>
          ) : (
            <>
              <Button onClick={() => navigate("/login")} color="inherit">
                Login
              </Button>
              <Button onClick={() => navigate("/signup")} color="inherit">
                SignUp
              </Button>
            </>
          )}
          {user && (
            <Box marginLeft={"auto"} display="flex" alignItems="center" gap={1}>
              <Tooltip title="Logout">
              <IconButton
                onClick={logout}
              >
                <Logout />
              </IconButton>
              </Tooltip>
            </Box>
          )}
        </Toolbar>
      </AppBar>
    </Box>
  );
};
