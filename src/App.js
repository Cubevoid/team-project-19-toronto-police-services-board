import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import { Navigation, Footer, Home, Agenda, Minutes, NotFound } from "./components";
import { Link, withRouter } from "react-router-dom";

function App() {
  return (
    <div className="App">
      <Router>
        <Navigation />
        <Switch>
          <Route exact path="/" component={() => <Home />}/>
          <Route exact path="/agenda" component={() => <Agenda />}/>
          <Route exact path="/minute" component={() => <Minutes />}/>
          <Route component={NotFound}/>
        </Switch>
      </Router>
    </div>
  );
}

export default App;
