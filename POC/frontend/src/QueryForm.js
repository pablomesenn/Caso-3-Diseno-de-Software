import { useState } from 'react';
import axios from 'axios';

function QueryForm({ token }) {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(
        '/api/query',
        { query },
        { headers: { Authorization: `Bearer ${token}` } }
      );
      setResults(response.data.results);
      setError('');
    } catch (err) {
      setError(err.response?.data?.message || 'Query failed');
    }
  };

  return (
    <div>
      <h2>Run Query</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="query">Query</label>
          <textarea
            id="query"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            required
            placeholder="Enter your query (e.g., SELECT *)"
            rows="4"
          />
        </div>
        <button type="submit" className="button button-primary">
          Submit Query
        </button>
      </form>
      {error && <div className="error">{error}</div>}
      {results.length > 0 && (
        <div className="results">
          <h3>Results</h3>
          <pre>{JSON.stringify(results, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default QueryForm;