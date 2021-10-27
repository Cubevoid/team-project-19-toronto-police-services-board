import React from "react";
import DOMPurify from 'dompurify';
import Parser from 'html-react-parser';

export default class FetchMinutes extends React.Component{
  state = {
    loading: true
  };

  async componentDidMount() {
    const url = 'http://127.0.0.1:8000/meetings/api/MeetingMinutes/'
    const response = await fetch(url);
    const data = await response.json();
    this.setState({meeting : data, loading : false});
  }

  render() {
    const newItems = this.state.meeting;

    if (this.state.loading) {
      return <div>loading...</div>;
    }

    if (!this.state.meeting) {
      return <div>didn't get a meeting</div>;
    }

    return newItems.map((item) => (
      <div>
        <div>Meeting: {item.meeting}</div>
        <div>Youtube Link: {item.yt_link}</div>
        <div>Notes: {Parser(DOMPurify.sanitize(item.notes))}</div>
        <br></br>
      </div>
    ));
  }
}
/*
Old code:

function Minutes() {
  return (
    <div className="contact">
      <div class="container">
        <div class="row align-items-center my-5">
          <div class="col-lg-7">
            <img
              class="img-fluid rounded mb-4 mb-lg-0"
              src="http://placehold.it/900x400"
              alt=""
            />
          </div>
          <div class="col-lg-5">
            <h1 class="font-weight-light">Minutes</h1>
            <p>
              Dummy text
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Minutes;
*/
