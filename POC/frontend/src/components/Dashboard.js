import { useEffect, useRef } from 'react';
import { Box, Typography } from '@mui/material';
import { toast } from 'react-toastify';

function Dashboard({ accessToken }) {
  const dashboardRef = useRef(null);

  useEffect(() => {
    const embedDashboard = async () => {
      if (!accessToken) return;
      try {
        // Fetch embedding URL from backend
        const res = await fetch('http://localhost:5000/api/dashboard-url/your_dashboard_id', {  // Replace with actual dashboard ID
          headers: {
            Authorization: `Bearer ${accessToken}`,
          },
        });
        if (!res.ok) throw new Error('Failed to fetch embed URL');
        const { embedUrl } = await res.json();

        // Embed dashboard using QuickSight Embedding SDK
        const containerDiv = dashboardRef.current;
        const options = {
          url: embedUrl,
          container: containerDiv,
          scrolling: 'auto',
          height: '400px',
          width: '100%',
        };
        window.QuickSightEmbedding.embedDashboard(options);
      } catch (err) {
        toast.error('Error al cargar el dashboard');
        console.error(err);
      }
    };
    embedDashboard();
  }, [accessToken]);

  return (
    <Box>
      <Typography variant="h5" gutterBottom>
        Dashboard de Datos
      </Typography>
      <div ref={dashboardRef} style={{ height: '400px', width: '100%' }} />
    </Box>
  );
}

export default Dashboard;