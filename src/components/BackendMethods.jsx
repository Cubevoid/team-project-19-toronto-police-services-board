import React from "react";

export default class BackendMethods {
  static PATH = '8000'

  static currentAdminUrl(item) {
    return window.location.hostname.includes("localhost") ? 'http://' + window.location.hostname + ':' + this.PATH + '/api/' + item : 'https://backend-smtcuvoqba-uc.a.run.app/' + 'api/' + item;
  }

  static async fetchItems(item) {
    const url = this.currentAdminUrl(item);
    var errors = false;
    const response = await fetch(url)
      .then(function (response) {
        if (!response.ok) {
          throw Error(response.statusText);
        }
        return response;
      }).catch(error => {
        errors = true;
      });

    const data = errors ? null : await response.json();
    return data;
  }
}
