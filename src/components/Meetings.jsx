import React, { Fragment } from "react";
import Minutes from "./Minutes";
import Agenda from "./Agenda";
import BackendMethods from "./BackendMethods";

class Meetings extends BackendMethods{

  constructor(props) {
    super(props);

    this.state = {
      data: {},
      loading: true,
      agenda: true
    };
    this.ITEM = "Meeting/"
  }

  subTextLabel() {
    return this.state.agenda ? 'Agenda' : 'Meeting Minutes';
  }

  displayAgendaOrMinutes() {
    return this.state.agenda ? <Agenda meetingId={this.state.currentMeeting.id}/> : <Minutes meetingId={this.state.currentMeeting.id}/>;
  }

  meetingLabel() {
    return this.state.currentMeeting.title;
  }

  setAgendaOpen() {
    this.setState({agenda: true});
  }

  setMinuteOpen() {
    this.setState({agenda: false});
  }

  setCurrentMeeting(meeting) {
    this.setState({currentMeeting: meeting});
  }

  displayMeetingDetails() {
    return <div className="meeting-details" border="1">
      <div className="agenda-minutes-header-left">
        <h1>{this.meetingLabel()}</h1>
      </div>
      <ul className="agenda-minutes-header-right">
        <li className="nav-agenda-minute-1">
          <a href="#" className="sub-nav-text" onClick={() => this.setAgendaOpen()}>
            Read Agenda
          </a>
        </li>
        <li className="nav-agenda-minute-1">
          <a href={this.state.currentMeeting.recording_link} className="sub-nav-text">
            View on Youtube
          </a>
        </li>
        <li className="nav-agenda-minute-1">
          <a href="#" className="sub-nav-text" onClick={() => this.setMinuteOpen()}>
            Read Minutes
          </a>
        </li>
      </ul>
      <h1 className="header">{this.subTextLabel()}</h1>
      <div className="meeting-text-output">
        {this.displayAgendaOrMinutes()}
      </div>
    </div>
  }

  render() {
    if (this.state.errors) {
      return <div>could not retrieve meeting information</div>
    }

    if (this.state.loading) {
      return <div></div>;
    }

    if (!this.state.data) {
      return <div>didn't get a meeting</div>;
    }

    return (
      <div className="meeting-info">
        <div className="meeting-table">
          <table border="1">
            <tbody>
              <tr>
                <th>Date</th>
                <th>Title</th>
                <th>Type</th>
              </tr>
              {this.state.data.sort((a, b) =>
                new Date(...b.date.substring(0, b.date.indexOf('T')).split('/').reverse()) -
                new Date(...a.date.substring(0, a.date.indexOf('T')).split('/').reverse())).map((meeting) => {
                return <Fragment>
                  <tr key={meeting.id} onClick={() => this.setCurrentMeeting(meeting)}>
                    <td>{meeting.date.substring(0, meeting.date.indexOf('T'))}</td>
                    <td>{meeting.title}</td>
                    <td>{meeting.meeting_type}</td>
                  </tr>
                </Fragment>
              })}
            </tbody>
          </table>
        </div>
        {this.state.currentMeeting && this.displayMeetingDetails()}
      </div>
    );
  }
}

export default Meetings;