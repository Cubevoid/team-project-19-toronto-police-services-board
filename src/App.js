import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import { Navigation, Home, Agenda, Minutes, NotFound } from "./components";

function App() {
  return (
    <div className="App">
      <Router>
        <Navigation />
        <Switch>
          <Route exact path="/" component={() => <Home />}/>
          <Route exact path="/agenda" component={() => <Agenda />}/>
          <Route exact path="/agenda/:meetingId" component={(props) => <Agenda {...props}/>}/>
          <Route exact path="/minute" component={() => <Minutes />}/>
          <Route exact path="/minutes/:meetingId" render={(props) => <Minutes {...props}/>}/>
          <Route component={NotFound}/>
        </Switch>
      </Router>
    </div>
  );
}

export default App;
