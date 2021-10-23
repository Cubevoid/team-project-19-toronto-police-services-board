import React from "react";

function Home() {
  return (
    <div className="home">
      <div className="container">
        <div className="align-items-center">
          <div className="main-icon">
            <img src={require('./../img/tpsb_icon.png').default} />
          </div>
          <div className="col-lg-5">
            <h1 class="font-weight-light">Home</h1>
            <p>
              Dummy text
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Home;
