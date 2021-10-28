import React from "react";
import DOMPurify from 'dompurify';
import Parser from 'html-react-parser';

export default class FetchMinutes extends React.Component{
  constructor(props) {
    super(props);

    this.state = {
      loading: true,
      errors: false
    };
  }

  currentAdminUrl() {
    return window.location.hostname.includes("localhost") ? 'http://' + window.location.hostname + ':8000/meetings/api/MeetingMinutes/' : 'https://backend-smtcuvoqba-uc.a.run.app/';
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
    this.setState({meeting : data, loading : false});
  }

  render() {
    const newItems = this.state.meeting;

    if (this.state.errors) {
      return <div>could not retrieve meeting minutes information</div>
    }

    if (this.state.loading) {
      return <div></div>;
    }

    if (!this.state.meeting) {
      return <div>didn't get a meeting</div>;
    }

    return newItems.filter(minute => minute.meeting === this.props.meetingId).map((item) => (
      <div>
        <div>MeetingId: {item.meeting}</div>
        <div><a href={item.yt_link}>Youtube Link</a></div>
        <div>Notes: {Parser(DOMPurify.sanitize(item.notes))}</div>
        <br></br>
      </div>
    ));
  }
}
