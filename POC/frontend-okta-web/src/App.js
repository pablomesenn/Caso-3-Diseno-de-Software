import React, { useState } from 'react';
import { OktaAuth } from '@okta/okta-auth-js';

const oktaAuth = new OktaAuth({
  issuer: `${process.env.REACT_APP_OKTA_DOMAIN}/oauth2/default`,
  clientId: process.env.REACT_APP_OKTA_CLIENT_ID,
  redirectUri: window.location.origin + '/login/callback',
  scopes: ['openid', 'profile', 'email'],
});

function App() {
  const [accessToken, setAccessToken] = useState(null);
  const [profile, setProfile] = useState(null);
  const [apiResponse, setApiResponse] = useState(null);

  const login = async () => {
    try {
      const tokens = await oktaAuth.token.getWithPopup();
      oktaAuth.tokenManager.setTokens(tokens);
      const userInfo = await oktaAuth.token.getUserInfo(tokens.accessToken);
      setAccessToken(tokens.accessToken.accessToken);
      setProfile(userInfo);
    } catch (err) {
      console.error('Login error:', err);
    }
  };

  const callBackend = async () => {
    if (!accessToken) return alert('Primero inicia sesión');

    try {
      const res = await fetch('http://localhost:5000/api/secure-data', {
        headers: {
          Authorization: `Bearer ${accessToken}`,
        },
      });
      const data = await res.json();
      setApiResponse(data);
    } catch (err) {
      console.error('API error:', err);
    }
  };

  const logout = async () => {
    await oktaAuth.signOut();
    setAccessToken(null);
    setProfile(null);
    setApiResponse(null);
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>React + Okta + Flask</h1>
      <button onClick={login}>Login</button>
      <button onClick={callBackend}>Llamar API Segura</button>
      <button onClick={logout}>Logout</button>

      {profile && <p>Hola, {profile.name}</p>}
      {apiResponse && <pre>{JSON.stringify(apiResponse, null, 2)}</pre>}
    </div>
  );
}

export default App;
