import { Home } from "./pages/Home";
import { Login } from "./pages/Login";
import { Profile } from "./pages/Profile";
import { SignUp } from "./pages/SignUp";
import { NotFound } from "./pages/NotFound";

export const routes = [{
        link: "/",
        name: "Home",
        isProtected: true,
        Component: Home,
    },
    {
        link: "/profile",
        name: "Profile",
        isProtected: true,
        Component: Profile,
    },
    {
        link: "/login",
        name: "Login",
        Component: Login,
    },
    {
        link: "/signup",
        name: "Signup",
        Component: SignUp,
    },
    {
        link: "*",
        name: "404",
        Component: NotFound,
    },
];