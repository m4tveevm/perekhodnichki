import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./components/Home";
import Quest from "./components/Quest/Quest";
import ExhibitsList from "./components/Exhibits/ExhibitsList";
import ExhibitDetail from "./components/Exhibits/ExhibitDetail";
import VirtualTour from "./components/VirtualTour/VirtualTour";
import Leaderboard from "./components/Leaderboard/Leaderboard";
import Achievements from "./components/Achievements/Achievements";
import Badges from "./components/Badges/Badges";
import LessonDetail from "./components/Lesson/LessonDetail";
import Events from "./components/Events/Events";
import Map from "./components/Map/Map";
import Feedback from "./components/Feedback/Feedback";
import Login from "./components/Auth/Login";
import Logout from "./components/Auth/Logout";
import PrivateRoute from "./context/PrivateRoute";
import UserProfile from "./components/User/UserProfile";
import UserSettings from "./components/User/UserSettings";
import NotFound from "./components/NotFound";
import Sidebar from "./components/Sidebar";
import { ToastContainer } from "react-toastify";
import "./index.css";
import "react-toastify/dist/ReactToastify.css";
import React from "react";


function App() {
  return (
    <Router>
      <Sidebar />
      <div className="content">
        <ToastContainer position="bottom-right" autoClose={3000} />
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route
            path="*"
            element={
              <PrivateRoute>
                <MainApp />
              </PrivateRoute>
            }
          />
        </Routes>
      </div>
    </Router>
  );
}

function MainApp() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/quest" element={<Quest />} />
      <Route path="/exhibits" element={<ExhibitsList />} />
      <Route path="/exhibits/:id" element={<ExhibitDetail />} />
      <Route path="/virtual-tour" element={<VirtualTour />} />
      <Route path="/leaderboard" element={<Leaderboard />} />
      <Route path="/achievements" element={<Achievements />} />
      <Route path="/badges" element={<Badges />} />
      <Route path="/events" element={<Events />} />
      <Route path="/map" element={<Map />} />
      <Route path="/feedback" element={<Feedback />} />
      <Route path="/profile" element={<UserProfile />} />
      <Route path="/settings" element={<UserSettings />} />
      <Route path="/logout" element={<Logout />} />
      <Route path="*" element={<NotFound />} />
    </Routes>
  );
}

export default App;
