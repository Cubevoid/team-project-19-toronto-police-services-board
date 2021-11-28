import React from "react";
import DOMPurify from 'dompurify';
import Parser from 'html-react-parser';
import BackendMethods from "./BackendMethods";

export default class FetchMinutes extends React.Component {
  constructor(props, match) {
    super(props);

    this.state = {
      loading: true,
      errors: false
    };
    this.ITEM = "Meeting/" + this.props.match.params.meetingId + "/Minutes/"
  }

  async componentDidMount() {
    const data = await BackendMethods.fetchItems(this.ITEM)
    if (!data) {
      this.setState({errors:true});
    }
    this.setState({ data: data});

    const meetingData = await BackendMethods.fetchItems("Meeting/" + this.props.match.params.meetingId + "/");
    if (!meetingData) {
      this.setState({errors:true});
    }
    this.setState({ meetingData: meetingData, loading: false });
  }

  render() {
    const newItems = this.state.data;

    if (this.state.errors) {
      return <div>could not retrieve meeting minutes information</div>
    }

    if (this.state.loading) {
      return <div></div>;
    }

    if (!this.state.data) {
      return <div>didn't get a meeting</div>;
    }

    return <div>
        <div className="agenda-title">
          <div className="flex"><img src={require('./../img/tpsb_icon.png').default} /></div>
          <br></br>
          <h1 style={{ textAlign: "Center" }}>Online Virtual Meeting</h1>
          <h1 style={{ textAlign: "Center" }}>{this.state.meetingData.date.substring(0, this.state.meetingData.date.indexOf('T')).split('/').reverse()}</h1>
          <h1 style={{ textAlign: "Center" }}>{this.state.meetingData.date.substring(this.state.meetingData.date.indexOf('T') + 1, this.state.meetingData.date.length).split('/').reverse()}</h1>
          <div className="flex"><img width="100%" src={require('./../img/tpsb_after_title.png').default} /></div>
          <br></br>
          <h2 style={{ textAlign: "Center" }}>Items Considered:</h2>
        </div>
        <div>MeetingId: {newItems.meeting}</div>
        <div>Notes: {Parser(DOMPurify.sanitize(newItems.notes))}</div>
        <br></br>
      </div>
  }
}
