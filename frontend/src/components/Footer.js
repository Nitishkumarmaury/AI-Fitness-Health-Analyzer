import React from 'react';
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';

function Footer() {
  return (
    <Box
      component="footer"
      sx={{
        py: 3,
        px: 2,
        mt: 'auto',
        background: 'linear-gradient(90deg, #6C63FF 0%, #FF6584 100%)',
        color: '#fff',
        boxShadow: '0 -2px 12px rgba(108,99,255,0.10)',
      }}
    >
      <Container maxWidth="lg">
        <Typography variant="body2" color="text.secondary" align="center">
          {'© '}
          {new Date().getFullYear()}
          {' AI Fitness Health Analyzer | Powered by Google Gemini AI'}
        </Typography>
      </Container>
    </Box>
  );
}

export default Footer;

