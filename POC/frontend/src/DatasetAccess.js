import { useState } from 'react';
import axios from 'axios';

function DatasetAccess({ token }) {
  const [datasetId, setDatasetId] = useState('');
  const [secret, setSecret] = useState('');
  const [shares, setShares] = useState([]);
  const [inputShares, setInputShares] = useState(['', '']);
  const [accessResult, setAccessResult] = useState('');
  const [error, setError] = useState('');

  const handleGenerateShares = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(
        `/api/generate-shares/${datasetId}`,
        { secret },
        { headers: { Authorization: `Bearer ${token}` } }
      );
      setShares(response.data.shares);
      setError('');
    } catch (err) {
      setError(err.response?.data?.message || 'Failed to generate shares');
    }
  };

  const handleAccessDataset = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(
        `/api/access-dataset/${datasetId}`,
        { shares: inputShares.filter((s) => s) },
        { headers: { Authorization: `Bearer ${token}` } }
      );
      setAccessResult(response.data.message + ': ' + response.data.secret);
      setError('');
    } catch (err) {
      setError(err.response?.data?.message || 'Failed to access dataset');
    }
  };

  return (
    <div>
      <h2>Access Dataset</h2>
      <form onSubmit={handleGenerateShares}>
        <div className="form-group">
          <label htmlFor="datasetId">Dataset ID</label>
          <input
            id="datasetId"
            type="text"
            value={datasetId}
            onChange={(e) => setDatasetId(e.target.value)}
            required
            placeholder="Enter dataset ID (e.g., dataset1)"
          />
        </div>
        <div className="form-group">
          <label htmlFor="secret">Secret</label>
          <input
            id="secret"
            type="text"
            value={secret}
            onChange={(e) => setSecret(e.target.value)}
            required
            placeholder="Enter secret"
          />
        </div>
        <button type="submit" className="button button-primary">
          Generate Shares
        </button>
      </form>
      {shares.length > 0 && (
        <div className="results">
          <h3>Generated Shares</h3>
          <pre>{shares.join('\n')}</pre>
        </div>
      )}
      <form onSubmit={handleAccessDataset}>
        <h3>Enter Shares</h3>
        {inputShares.map((share, index) => (
          <div className="form-group" key={index}>
            <label htmlFor={`share${index}`}>Share {index + 1}</label>
            <input
              id={`share${index}`}
              type="text"
              value={share}
              onChange={(e) => {
                const newShares = [...inputShares];
                newShares[index] = e.target.value;
                setInputShares(newShares);
              }}
              placeholder="Enter share (e.g., 1:xxxx...)"
            />
          </div>
        ))}
        <button type="submit" className="button button-primary">
          Access Dataset
        </button>
      </form>
      {accessResult && <div className="message">{accessResult}</div>}
      {error && <div className="error">{error}</div>}
    </div>
  );
}

export default DatasetAccess;