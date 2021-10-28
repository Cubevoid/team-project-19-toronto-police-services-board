import React from "react";

export default class Agenda extends React.Component{
  state = {
    loading: true,
    errors: false
  };

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
    this.setState({meeting : data, loading : false});
  }

  render() {
    const newItems = this.state.meeting;

    if (this.state.errors) {
      return <div>could not retrieve agenda information</div>
    }

    if (this.state.loading) {
      return <div>loading...</div>;
    }

    if (!this.state.meeting) {
      return <div>didn't get an agenda</div>;
    }

    return newItems.map((item) => (
      <div>
        <div>Meeting: {item.meeting}</div>
        <br></br>
      </div>
    ));
  }
}
