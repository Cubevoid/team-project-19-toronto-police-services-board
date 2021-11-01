import React from "react";
import DOMPurify from 'dompurify';
import Parser from 'html-react-parser';
import BackendMethods from "./BackendMethods";

export default class FetchMinutes extends BackendMethods{
  constructor(props) {
    super(props);

    this.state = {
      loading: true,
      errors: false
    };
    this.ITEM = "Minutes/"
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

    return newItems.filter(minute => minute.meeting === this.props.meetingId).map((item) => (
      <div>
        <div>MeetingId: {item.meeting}</div>
        <div>Notes: {Parser(DOMPurify.sanitize(item.notes))}</div>
        <br></br>
      </div>
    ));
  }
}
