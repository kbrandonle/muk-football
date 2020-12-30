import React from "react";

class Login extends React.Component {
  constructor() {
    super();
    this.emailInputRef = React.createRef();
    this.passwordInputRef = React.createRef();
    this.state = {};
  }

  render() {
    return (
      <div>
        <center>
          <form id="loginInterface" onSubmit={this.handleLoginSubmit}>
            <label htmlFor="emailInput" style={{ padding: 0, fontSize: 24 }}>
              Email:
              <input
                ref={this.emailInputRef}
                className="form-control login-text"
                type="email"
                placeholder="Enter Email Address"
                id="emailInput"
                pattern="[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
                required={true}
              />
            </label>
            <p />
            <label htmlFor="passwordInput" style={{ padding: 0, fontSize: 24 }}>
              Password:
              <input
                ref={this.passwordInputRef}
                className="form-control login-text"
                type="password"
                id="passwordInput"
                placeholder="Enter Password"
                pattern=""
                required={true}
              />
            </label>
            <p className="bg-danger" id="feedback" style={{ fontSize: 16 }} />
            <button
              id="loginBtn"
              type="submit"
              className="btn-color-theme btn btn-primary btn-block login-btn"
            >
              <span id="login-btn-icon" />
              &nbsp;Login
            </button>
            <p>
              <button type="button" className="btn btn-link login-link">
                Create an account
              </button>{" "}
              |
              <button type="button" className="btn btn-link login-link">
                Reset your password
              </button>
            </p>
          </form>
        </center>
      </div>
    );
  }
}

export default Login;
