import React from "react";
import AgendaItem from "./AgendaItem.jsx"

export default class Agenda extends React.Component{
  constructor(props) {
    super(props);

    this.state = {
      loading: true,
      errors: false
    };
  }

  currentAdminUrl() {
    return window.location.hostname.includes("localhost") ? 'http://' + window.location.hostname + ':8000/meetings/api/Agenda/' : 'https://backend-smtcuvoqba-uc.a.run.app/';
  }

  async componentDidMount() {
    const url = this.currentAdminUrl();
    const response = await fetch(url)
      .then(function(response) {
        if (!response.ok) {
          throw Error(response.statusText);
        }
        return response;
      }).catch(error => {
        this.setState({errors : true})
      });

    const data = this.state.errors ? null : await response.json();
    this.setState({agenda : data, loading : false});
  }

  render() {
    if (this.state.errors) {
      return <div>could not retrieve agenda information</div>
    }

    if (this.state.loading) {
      return <div></div>;
    }

    if (!this.state.agenda) {
      return <div>didn't get an agenda</div>;
    }

    return this.state.agenda.filter(agenda => agenda.meeting === this.props.meetingId).map((item) => (
      <div>
        <div>MeetingId: {item.meeting}</div>
        <AgendaItem agendaId={item.id}/>
        <br></br>
      </div>
    ));
  }
}
