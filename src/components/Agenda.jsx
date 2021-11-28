import React from "react";
import AgendaItem from "./AgendaItem.jsx"
import BackendMethods from "./BackendMethods.jsx";

export default class Agenda extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      loading: true,
      errors: false
    };

    this.ITEM = "Meeting/" + this.props.match.params.meetingId + "/Agenda/"
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
    if (this.state.errors) {
      return <div>could not retrieve agenda information</div>
    }

    if (this.state.loading) {
      return <div></div>;
    }

    if (!this.state.data) {
      return <div>didn't get an agenda</div>;
    }

    return <div>
        <div className="agenda-title">
          <div className="flex"><img src={require('./../img/tpsb_icon.png').default} /></div>
          <br></br>
          <h1 style={{ textAlign: "Center" }}>Online Virtual Meeting</h1>
          <h1 style={{ textAlign: "Center" }}>{this.state.meetingData.date.substring(0, this.state.meetingData.date.indexOf('T')).split('/').reverse()}</h1>
          <h1 style={{ textAlign: "Center" }}>At {this.state.meetingData.date.substring(this.state.meetingData.date.indexOf('T') + 1, this.state.meetingData.date.length).split('-')[0]}</h1>
          <div className="flex"><img width="100%" src={require('./../img/tpsb_after_title.png').default} /></div>
          <br></br>
          <h2 style={{ textAlign: "Center" }}>Items for consideration:</h2>
        </div>
        <div>

          <AgendaItem agenda={this.state.data[0]}/>
        </div>
        <br></br>
      </div>;
  }
}
