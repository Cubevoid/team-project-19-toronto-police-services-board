import React, {useState} from "react";
import { Link, withRouter } from "react-router-dom";

function NavItem(props) {

const [open, setOpen] = useState(false);

  return (
    <li className="nav-item">

      <a href="#" className="icon-button" onClick={() => setOpen(!open)}>
        {props.text}
      </a>

      {open && props.children}
    </li>
  );
}

function DropdownMenu() {

  function DropdownItem(props) {
    return (
      <Link className="menu-item" to={props.link}>
        {props.children}
      </Link>
    )
  }

  return (
    <div className="dropdown">
      <DropdownItem link="/">Home</DropdownItem>
      <DropdownItem link="/agenda">Agenda</DropdownItem>
      <DropdownItem link="/minute">Minute</DropdownItem>
    </div>
  );
}

function DropdownName(props) {
  var text = props.text.replace("/", "");
  if (text === "") {
    text = "Home"
  } else {
    text = text.charAt(0).toUpperCase() + text.slice(1);
  }
  return text;
}

function Navigation(props) {
  return (
    <div className="navigation">
      <nav className="navbar">
        <ul className="navbar-nav">
          <NavItem text = <DropdownName text = {window.location.pathname}/>>
            <DropdownMenu />
          </NavItem>
        </ul>
      </nav>
    </div>
  );
}

export default withRouter(Navigation);
