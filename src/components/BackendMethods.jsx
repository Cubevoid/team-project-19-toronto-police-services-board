import React from "react";

export default class BackendMethods extends React.Component {
  PATH = '8000'
  ITEM = 'Meeting/'
  SUBITEM = ''
  SUBSUBITEM = ''
  currentAdminUrl() {
    return window.location.hostname.includes("localhost") ? 'http://' + window.location.hostname + ':' + this.PATH + '/api/' + this.ITEM + this.SUBITEM + this.SUBSUBITEM : 'https://backend-smtcuvoqba-uc.a.run.app/' + 'api/' + this.ITEM;
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
