import React from "react";
import AgendaItem from "./AgendaItem.jsx"
import BackendMethods from "./BackendMethods.jsx";

export default class Agenda extends BackendMethods{
  constructor(props) {
    super(props);

    this.state = {
      loading: true,
      errors: false
    };
    this.ITEM = "Agenda/"
  }

  render() {
    if (this.state.errors) {
      return <div>could not retrieve agenda information</div>
    }

    if (this.state.loading) {
      return <div></div>;
    }

    if (!this.state.data) {
      return <div>didn't get an agenda</div>;
    }

    return this.state.data.filter(data => data.meeting === Number(this.props.match.params.meetingId)).map((item) => (
      <div>
        <AgendaItem agendaId={item.id}/>
        <br></br>
      </div>
    ));
  }
}
