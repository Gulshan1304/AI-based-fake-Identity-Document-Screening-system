import React, { useState } from "react";

function UploadBox({ onFileSelect }) {

  const [file, setFile] = useState(null);
  const [dragging, setDragging] = useState(false);


  const handleFile = (selectedFile) => {

    if (!selectedFile) return;

    setFile(selectedFile);

    if (onFileSelect) {
      onFileSelect(selectedFile);
    }
  };


  const handleInputChange = (event) => {

    const selectedFile =
      event.target.files[0];

    handleFile(selectedFile);
  };


  const handleDrop = (event) => {

    event.preventDefault();

    setDragging(false);

    const droppedFile =
      event.dataTransfer.files[0];

    handleFile(droppedFile);
  };


  return (

    <div
      className={`upload-box ${
        dragging ? "dragging" : ""
      }`}
      onDragOver={(event) => {
        event.preventDefault();
        setDragging(true);
      }}
      onDragLeave={() => setDragging(false)}
      onDrop={handleDrop}
    >

      <input
        type="file"
        id="document-upload"
        hidden
        accept=".pdf,.jpg,.jpeg,.png"
        onChange={handleInputChange}
      />


      {!file ? (

        <label
          htmlFor="document-upload"
          className="upload-content"
        >

          <div className="upload-icon">
            ↑
          </div>

          <h3>
            Upload Identity Document
          </h3>

          <p>
            Drag & drop your document here
            or click to browse
          </p>

          <span>
            PDF, JPG, JPEG or PNG
          </span>

          <small>
            Maximum file size: 10 MB
          </small>

        </label>

      ) : (

        <div className="selected-file">

          <div className="file-icon">
            ▣
          </div>

          <div className="file-details">

            <strong>
              {file.name}
            </strong>

            <span>
              {(file.size / 1024 / 1024).toFixed(2)}
              {" "}MB
            </span>

          </div>

          <button
            className="remove-file"
            onClick={() => {
              setFile(null);
              onFileSelect?.(null);
            }}
          >
            ×
          </button>

        </div>

      )}

    </div>

  );
}

export default UploadBox;