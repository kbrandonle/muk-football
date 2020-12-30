import logo from "../logo.svg";
import React from "react";
import AppMode from "../Page";
import Login from "./Login";
import Team from "./ManageTeam";
import "../App.css";

const modeToPage = {};
modeToPage[AppMode.LOGIN] = Login;
modeToPage[AppMode.TEAM] = Team;

class App extends React.Component {
  constructor() {
    super();
    this.state = {
      mode: AppMode.LOGIN,
    };
  }

  changePage = (newPage) => {
    this.setState({
      mode: newPage,
    });
  };

  render() {
    const CurrentPage = modeToPage[this.state.mode];
    return (
      <div>
        <CurrentPage changePage={this.changePage} />
      </div>
    );
  }
}

export default App;
