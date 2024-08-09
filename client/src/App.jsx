import { AppRouter } from "./AppRouter";
import { AuthProvider } from "./AuthContext";
import BackgroundSlider from "./components/BackgroundSlider/BackgroundSlider";
import { SnackbarProvider } from "./SnackbarContext";
import {  ThemeProvider, createTheme } from "@mui/material/styles";

export const theme = createTheme({
  palette: {
    primary: {
      main: "#00897b",
    },
  },
});


function App() {
  return (
    <div className="App">
      <ThemeProvider theme={theme}>
        <AuthProvider>
          <SnackbarProvider>
            <BackgroundSlider />
            <AppRouter />
          </SnackbarProvider>
        </AuthProvider>
      </ThemeProvider>
    </div>
  );
}

export default App;
