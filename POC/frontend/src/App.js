import { useState } from 'react';
import { Security, LoginCallback } from '@okta/okta-react';
import { OktaAuth, toRelativeUrl } from '@okta/okta-auth-js';
import { BrowserRouter as Router, Route, Routes, useNavigate } from 'react-router-dom';
import { Container, Typography, Button, AppBar, Toolbar } from '@mui/material';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import Dashboard from './components/Dashboard';
import QueryForm from './components/QueryForm';

const oktaAuth = new OktaAuth({
  issuer: 'https://dev-w425j2q1a431gpdw.us.okta.com/oauth2/default',
  clientId: 'AzrNIzpdapSkqzh4q1zUJRYZUX3KsXlD',
  redirectUri: window.location.origin + '/login/callback',
  scopes: ['openid', 'profile', 'email'],
});

function App() {
  const navigate = useNavigate();
  const [authState, setAuthState] = useState(null);

  const restoreOriginalUri = async (_oktaAuth, originalUri) => {
    navigate(toRelativeUrl(originalUri || '/', window.location.origin));
  };

  const login = async () => {
    try {
      await oktaAuth.signInWithRedirect();
    } catch (err) {
      toast.error('Error al iniciar sesión');
    }
  };

  const logout = async () => {
    try {
      await oktaAuth.signOut();
      setAuthState(null);
      toast.success('Sesión cerrada');
    } catch (err) {
      toast.error('Error al cerrar sesión');
    }
  };

  oktaAuth.authStateManager.subscribe((newAuthState) => {
    setAuthState(newAuthState);
  });

  return (
    <Security oktaAuth={oktaAuth} restoreOriginalUri={restoreOriginalUri}>
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6" style={{ flexGrow: 1 }}>
            Data Pura Vida
          </Typography>
          {authState?.isAuthenticated ? (
            <Button color="inherit" onClick={logout}>
              Logout
            </Button>
          ) : (
            <Button color="inherit" onClick={login}>
              Login
            </Button>
          )}
        </Toolbar>
      </AppBar>
      <Container maxWidth="lg" style={{ padding: 20 }}>
        <Routes>
          <Route path="/login/callback" element={<LoginCallback />} />
          <Route path="/" element={
            <>
              {authState?.isAuthenticated ? (
                <>
                  <Typography variant="h6" gutterBottom>
                    Hola, {authState.idToken.claims.name}
                  </Typography>
                  <Dashboard accessToken={authState?.accessToken?.accessToken} />
                  <QueryForm accessToken={authState?.accessToken?.accessToken} />
                </>
              ) : (
                <Typography variant="body1">Por favor, inicia sesión para continuar.</Typography>
              )}
            </>
          } />
        </Routes>
        <ToastContainer />
      </Container>
    </Security>
  );
}

export default function AppWrapper() {
  return (
    <Router>
      <App />
    </Router>
  );
}