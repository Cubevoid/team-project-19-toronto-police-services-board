import React from "react";
import DOMPurify from 'dompurify';
import Parser from 'html-react-parser';

export default class AgendaItem extends React.Component{
  constructor(props) {
    super(props);

    this.state = {
      loading: true,
      errors: false
    };
  }

  currentAdminUrl() {
    return window.location.hostname.includes("localhost") ? 'http://' + window.location.hostname + ':8000/meetings/api/AgendaItem/' : 'https://backend-smtcuvoqba-uc.a.run.app/';
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
    this.setState({agendaItem : data, loading : false});
  }

  render() {

    if (this.state.errors) {
      return <div>could not retrieve agenda information</div>
    }

    if (this.state.loading) {
      return <div></div>;
    }

    if (!this.state.agendaItem) {
      return <div>didn't get an agenda</div>;
    }

    return this.state.agendaItem.filter(agendaItem => agendaItem.agenda === this.props.agendaId).map((item) => (
      <div>
        <div>AgendaId: {item.agenda}</div>
        <div>Title: {item.title}</div>
        <div> {Parser(DOMPurify.sanitize(item.description))}</div>
        <div>Result: {item.result}</div>
        <div>Motion: {Parser(DOMPurify.sanitize(item.motion))}</div>
        <a className="download-attach" href={item.file} download>{item.file ? item.file.split('/').pop() : item.file}</a>
        <br></br>
      </div>
    ));
  }
}
