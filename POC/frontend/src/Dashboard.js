import { useState } from 'react';
import axios from 'axios';

function Dashboard({ token }) {
  const [datasetId, setDatasetId] = useState('');
  const [embedUrl, setEmbedUrl] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.get(`/api/dashboard-url/${datasetId}`, {
        headers: { Authorization: `Bearer ${token}` },
      });
      setEmbedUrl(response.data.embedUrl);
      setError('');
    } catch (err) {
      setError(err.response?.data?.message || 'Failed to get dashboard');
    }
  };

  return (
    <div>
      <h2>View Dashboard</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="dashboardDatasetId">Dataset ID</label>
          <input
            id="dashboardDatasetId"
            type="text"
            value={datasetId}
            onChange={(e) => setDatasetId(e.target.value)}
            required
            placeholder="Enter dataset ID (e.g., dataset1)"
          />
        </div>
        <button type="submit" className="button button-primary">
          Get Dashboard
        </button>
      </form>
      {embedUrl && (
        <div className="results">
          <h3>Dashboard URL</h3>
          <a href={embedUrl} target="_blank" rel="noopener noreferrer">
            {embedUrl}
          </a>
          <div style={{ marginTop: '1rem' }}>
            <img
              src="https://via.placeholder.com/600x400?text=Mock+Dashboard"
              alt="Mock Dashboard"
              style={{ width: '100%', borderRadius: '4px' }}
            />
          </div>
        </div>
      )}
      {error && <div className="error">{error}</div>}
    </div>
  );
}

export default Dashboard;