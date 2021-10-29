import React from "react";

export default class BackendMethods extends React.Component {
  PATH = '8080'
  ITEM = 'AgendaItem/'
  currentAdminUrl() {
    return window.location.hostname.includes("localhost") ? 'http://' + window.location.hostname + ':' + this.PATH + '/backend/api/' + this.ITEM : 'https://backend-smtcuvoqba-uc.a.run.app/' + '/backend/api/' + this.ITEM;
  }

  async componentDidMount() {
    const url = this.currentAdminUrl();
    const response = await fetch(url)
      .then(function (response) {
        if (!response.ok) {
          throw Error(response.statusText);
        }
        return response;
      }).catch(error => {
        this.setState({ errors: true })
      });

    const data = this.state.errors ? null : await response.json();
    this.setState({ data: data, loading: false });
  }
}
