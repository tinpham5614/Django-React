import React, { Component } from "react";
import { createRoot } from 'react-dom/client';

class App extends Component {
  render() {
    return (
      <div>
        <h1>Music Controller</h1>
      </div>
    );
  }
}

export default App;

const appDiv = document.getElementById("app");
const root = createRoot(appDiv);
root.render(<App />);