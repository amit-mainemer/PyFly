import React, {
  createContext,
  useContext,
  useState,
} from "react";
import { Snackbar, Alert } from "@mui/material";

const SnackbarContext = createContext();

export const SnackbarProvider = ({ children }) => {
  const [open, setOpen] = useState(false);
  const [message, setMessage] = useState(false);
  const [severity, setSeverity] = useState(false);

  const pop = (params) => {
    setOpen(true);
    setMessage(params.message);
    setSeverity(params.severity);
  };
  return (
    <SnackbarContext.Provider value={{ pop }}>
      {children}
      <Snackbar open={open} autoHideDuration={4000} onClose={() => setOpen(false)}  anchorOrigin={{ vertical: "top", horizontal: "center" }}>
        <Alert
          severity={severity}
          variant="filled"
          sx={{ width: "100%" }}
        >
          {message}
        </Alert>
      </Snackbar>
    </SnackbarContext.Provider>
  );
};

export const useSnackbar = () => useContext(SnackbarContext);
