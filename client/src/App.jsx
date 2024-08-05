import { AppRouter } from "./AppRouter";
import { AuthProvider } from "./AuthContext";
import BackgroundSlider from "./components/BackgroundSlider/BackgroundSlider";
import { SnackbarProvider } from "./SnackbarContext";

function App() {
  return (
    <div className="App">
      <AuthProvider>
        <SnackbarProvider>
          <BackgroundSlider />
          <AppRouter />
        </SnackbarProvider>
      </AuthProvider>
    </div>
  );
}

export default App;
