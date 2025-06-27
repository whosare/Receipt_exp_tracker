import React, { useState } from 'react';
import axios from 'axios';

function UploadReceipt() {
  const [file, setFile] = useState(null);
  const [response, setResponse] = useState(null);
  const [error, setError] = useState('');

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    setResponse(null);
    setError('');
  };

  const handleUpload = async () => {
    if (!file) {
      setError("Please select a file.");
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      const token = localStorage.getItem('token');
      const res = await axios.post('http://127.0.0.1:8000/upload-receipt', formData, {
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'multipart/form-data'
        }
      });

      setResponse(res.data);
    } catch (err) {
      console.error(err);
      setError("Upload failed. Check the file type and try again.");
    }
  };
  return (
    <div className="text-2xl text-center text-green-600 mt-20">Register Page</div>
  );
  return (
    <div>
      <h2>Upload Receipt</h2>
      <input type="file" onChange={handleFileChange} accept="image/*,.pdf" /><br /><br />
      <button onClick={handleUpload}>Upload</button>

      {error && <p style={{ color: 'red' }}>{error}</p>}
      {response && (
        <div>
          <h3>Parsed Receipt Info</h3>
          <pre>{JSON.stringify(response, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}


export default UploadReceipt;
