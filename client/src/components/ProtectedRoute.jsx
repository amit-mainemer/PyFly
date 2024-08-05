import { Navigate, Outlet } from "react-router-dom";
import { useAuth } from "../AuthContext";

export const ProtectedRoute = () => {
  const { auth } = useAuth();
  // If not authenticated, redirect to the login page
  if (!auth) {
    return <Navigate to="/login" />;
  }

  // Render the child components if authenticated
  return <Outlet />;
};
