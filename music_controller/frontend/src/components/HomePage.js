import React from "react";
import {
  Route,
  BrowserRouter as Router,
  Switch,
  Link,
  Redirect,
  Routes,
} from "react-router-dom";
import RoomJoinPage from "./RoomJoinPage";
import CreateRoomPage from "./CreateRoomPage";

export default function HomePage() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<h1>Home Page</h1>} />
        <Route path="/join" element={<RoomJoinPage />} />
        <Route path="/create" element={<CreateRoomPage />} />
      </Routes>
    </Router>
  );
}
