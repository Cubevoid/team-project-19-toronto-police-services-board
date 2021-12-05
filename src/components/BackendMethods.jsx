export default class BackendMethods {
  static PATH = process.env.REACT_APP_DEVELOPMENT_BACKEND_PORT

  static currentAdminUrl(item) {
    return (window.location.hostname.includes("localhost") && process.env.REACT_APP_ALWAYS_USE_DEPLOYMENT_URL === 'false') ? 'http://' + window.location.hostname + ':' + this.PATH + '/api/' + item : process.env.REACT_APP_DEPLOYMENT_URL + '/api/' + item;
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
