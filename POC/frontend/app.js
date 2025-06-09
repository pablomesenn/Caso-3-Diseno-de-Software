import React from 'react';
import {View, Button, StyleSheet, Text} from 'react-native';
import {authorize} from 'react-native-app-auth';

const config = {
  issuer: 'https://dev-w425j2q1a431gpdw.us.okta.com/oauth2/default',
  clientId: 'AzrNIzpdapSkqzh4q1zUJRYZUX3KsXlD',
  redirectUrl: 'com.poc.okta:/callback',
  scopes: ['openid', 'profile', 'email'],
  serviceConfiguration: {
    authorizationEndpoint: 'https://dev-w425j2q1a431gpdw.us.okta.com/oauth2/default/v1/authorize',
    tokenEndpoint: 'https://dev-w425j2q1a431gpdw.us.okta.com/oauth2/default/v1/token',
    revocationEndpoint: 'https://dev-w425j2q1a431gpdw.us.okta.com/oauth2/default/v1/revoke',
  },
};

export default function App() {
  const [token, setToken] = React.useState(null);

  const handleLogin = async () => {
    try {
      const result = await authorize(config);
      setToken(result.accessToken);
      console.log("Token:", result.accessToken);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <View style={styles.container}>
      <Button title="Iniciar sesión con Okta" onPress={handleLogin} />
      {token && <Text style={styles.token}>Token: {token.slice(0, 20)}...</Text>}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {flex: 1, justifyContent: 'center', alignItems: 'center'},
  token: {marginTop: 20, padding: 10},
});
