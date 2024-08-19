import React from "react";
import { Box, Typography, Button } from "@mui/material";
import { useNavigate } from "react-router-dom";

export const NotFound = () => {
  const navigate = useNavigate();
  return (
    <Box
      style={{
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        height: "calc(100% - 60px)",
      }}
    >
      <Box class="t-card">
        <Typography variant="h6">
          404, maybe try a different route...
        </Typography>
        <Button
          variant="contained"
          style={{ marginLeft: "auto", marginTop: 10 }}
          onClick={() => navigate("/")}
        >
          Home
        </Button>
      </Box>
    </Box>
  );
};
