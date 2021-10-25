import React, { useState } from "react";
import { Document, Page, pdfjs } from 'react-pdf/dist/umd/entry.webpack';
import test from './../img/test.pdf';
pdfjs.GlobalWorkerOptions.workerSrc = `//cdnjs.cloudflare.com/ajax/libs/pdf.js/${pdfjs.version}/pdf.worker.js`;

function DisplayPDF() {
  const [numPages, setNumPages] = useState(null);
  const [pageNumber, setPageNumber] = useState(1);

  function onDocumentLoadSuccess({ numPages }) {
    setNumPages(numPages);
  }

  return (
    <div>
      <Document
        file={test}
        onLoadSuccess={onDocumentLoadSuccess}
      >
        <Page pageNumber={pageNumber} />
      </Document>
      <p>Page {pageNumber} of {numPages}</p>
    </div>
  );
}

function Agenda() {
  return (
    <div className="about">
      <div className="container">
        <div className="row align-items-center my-5">
          <div className="col-lg-7">
            <img src={require('./../img/agenda.png').default} />
          </div>
          <div className="col-lg-5">
            <h1 className="font-weight-light">Agendas</h1>
            <p>
              <a href={test} download="test.pdf">Click to download</a>
            </p>
            <DisplayPDF />
          </div>
        </div>
      </div>
    </div>
  );
}

export default Agenda;
