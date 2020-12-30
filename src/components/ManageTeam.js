import React from "react";

class ManageTeam extends React.Component {
  constructor() {
    super();
    this.state = {
      starters: [],
      bench: [],
    };
  }
  render() {
    return (
      <div>
        <center>
          <h3>Team</h3>
        </center>
      </div>
    );
  }
}

export default ManageTeam;
