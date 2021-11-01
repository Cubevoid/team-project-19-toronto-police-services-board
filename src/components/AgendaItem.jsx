import React from "react";
import DOMPurify from 'dompurify';
import Parser from 'html-react-parser';
import BackendMethods from "./BackendMethods";

export default class AgendaItem extends BackendMethods{

  constructor(props) {
    super(props);

    this.state = {
      loading: true,
      errors: false
    };
    this.ITEM = 'AgendaItem/'
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

    return this.state.data.filter(data => data.agenda === this.props.agendaId).map((item) => (
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
