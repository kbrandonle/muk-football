import React, { useEffect } from "react";

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
          <div className="manage-team-container">
            <div>
              <h1 className="manage-team-title">Team</h1>
              <button className="edit-team-btn">Edit Team</button>
            </div>
          </div>
        </center>
        <center>
          <h3>Starters</h3>
        </center>

        <table className="table ">
          <thead className="thead-dark">
            <tr>
              <th scope="col">Name</th>
              <th scope="col">Position</th>
            </tr>
          </thead>
        </table>
        <center>
          <h3>Bench</h3>
        </center>
        <table class="table">
          <thead class="thead-dark">
            <tr>
              <th scope="col">Name</th>
              <th scope="col">Position</th>
            </tr>
          </thead>
          <tbody></tbody>
        </table>
      </div>
    );
  }
}

export default ManageTeam;
