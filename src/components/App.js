import logo from "../logo.svg";
import AppMode from "../Page";
import Login from "./Login";
import "../App.css";
import React, { useState, useEffect } from "react";

const modeToPage = {};
modeToPage[AppMode.LOGIN] = Login;

class App extends React.Component {
  constructor() {
    super();
    this.state = {
      mode: AppMode.LOGIN,
    };
  }

  render() {
    const CurrentPage = modeToPage[this.state.mode];
    return (
      <div>
        <CurrentPage />
      </div>
    );
  }
}

export default App;
