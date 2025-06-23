import { useState } from 'react';
import Login from './Login';
import QueryForm from './QueryForm';
import DatasetAccess from './DatasetAccess';
import Dashboard from './Dashboard';
import './styles.css';

function App() {
  const [token, setToken] = useState(localStorage.getItem('token') || '');
  const [userName, setUserName] = useState(localStorage.getItem('userName') || '');

  const handleLogin = (newToken, name) => {
    setToken(newToken);
    setUserName(name);
    localStorage.setItem('token', newToken);
    localStorage.setItem('userName', name);
  };

  const handleLogout = () => {
    setToken('');
    setUserName('');
    localStorage.removeItem('token');
    localStorage.removeItem('userName');
  };

  return (
    <div>
      {token ? (
        <>
          <nav className="nav">
            <div className="nav-title">Data Pura Vida - {userName}</div>
            <button className="nav-button" onClick={handleLogout}>
              Log Out
            </button>
          </nav>
          <div className="container">
            <QueryForm token={token} />
            <DatasetAccess token={token} />
            <Dashboard token={token} />
          </div>
        </>
      ) : (
        <div className="container">
          <Login onLogin={handleLogin} />
        </div>
      )}
    </div>
  );
}

export default App;