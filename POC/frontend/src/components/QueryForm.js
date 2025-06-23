import { useState } from 'react';
import { TextField, Button, Box, Typography } from '@mui/material';
import { toast } from 'react-toastify';

function QueryForm({ accessToken }) {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState(null);

  const submitQuery = async () => {
    if (!accessToken) {
      toast.error('Primero inicia sesión');
      return;
    }
    try {
      const res = await fetch('http://localhost:5000/api/query', {
        method: 'POST',
        headers: {
          Authorization: `Bearer ${accessToken}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query }),
      });
      if (!res.ok) throw new Error('Query failed');
      const data = await res.json();
      setResults(data);
      toast.success('Consulta ejecutada con éxito');
    } catch (err) {
      toast.error(`Error: ${err.message}`);
    }
  };

  return (
    <Box mt={4}>
      <Typography variant="h5" gutterBottom>
        Consultar Datos
      </Typography>
      <TextField
        fullWidth
        label="Ingresa tu consulta (ej. Muestra las ventas de 2025)"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        variant="outlined"
        margin="normal"
        inputProps={{ 'aria-label': 'Consulta de datos' }}
      />
      <Button variant="contained" onClick={submitQuery} sx={{ mt: 2 }}>
        Ejecutar Consulta
      </Button>
      {results && (
        <Box mt={2}>
          <Typography variant="h6">Resultados:</Typography>
          <pre>{JSON.stringify(results, null, 2)}</pre>
        </Box>
      )}
    </Box>
  );
}

export default QueryForm;