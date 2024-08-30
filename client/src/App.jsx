import { AppRouter } from "./AppRouter";
import { AuthProvider } from "./AuthContext";
import { BackgroundSliderCustom } from "./components/BackgroundSlider/BackgroundSlider";
import { SnackbarProvider } from "./SnackbarContext";
import { ThemeProvider, createTheme } from "@mui/material/styles";

export const theme = createTheme({
  palette: {
    primary: {
      main: "#00897b",
      // main: "#ffb300",
    },
  },
});

function App() {
  return (
    <div className="App">
      <ThemeProvider theme={theme}>
        <AuthProvider>
          <SnackbarProvider>
            <BackgroundSliderCustom />
            <AppRouter />
          </SnackbarProvider>
        </AuthProvider>
      </ThemeProvider>
    </div>
  );
}

export default App;
