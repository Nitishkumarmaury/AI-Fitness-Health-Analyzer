import React from 'react';
import { Container, Typography, Paper, Box, Grid } from '@mui/material';
import FitnessCenterIcon from '@mui/icons-material/FitnessCenter';
import VerifiedUserIcon from '@mui/icons-material/VerifiedUser';
import DataSaverOnIcon from '@mui/icons-material/DataSaverOn';

const AboutPage = () => {
  return (
    <Container maxWidth="md">
      <Box textAlign="center" mb={6}>
        <Typography variant="h3" component="h1" gutterBottom>
          About AI Fitness Health Analyzer
        </Typography>
        <Typography variant="h6" color="textSecondary">
          Using advanced AI to transform your fitness data into actionable insights
        </Typography>
      </Box>

      <Paper elevation={3} sx={{ p: 4, mb: 4 }}>
        <Typography variant="h5" component="h2" gutterBottom>
          Our Mission
        </Typography>
        <Typography variant="body1" paragraph>
          AI Fitness Health Analyzer is designed to help individuals make sense of their fitness data 
          through advanced AI analysis. We believe that understanding your fitness metrics is the first 
          step toward achieving your health goals.
        </Typography>
        <Typography variant="body1" paragraph>
          Our application uses Google's Gemini 1.5-flash AI model to analyze fitness data from uploaded 
          images, providing personalized recommendations and insights that empower you to make informed 
          decisions about your health journey.
        </Typography>
      </Paper>

      <Grid container spacing={4} mb={4}>
        <Grid item xs={12} md={4}>
          <Paper elevation={3} sx={{ p: 3, height: '100%', display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
            <FitnessCenterIcon color="primary" sx={{ fontSize: 60, mb: 2 }} />
            <Typography variant="h6" gutterBottom align="center">
              Data-Driven Insights
            </Typography>
            <Typography variant="body2" align="center">
              Our AI analyzes your fitness data to provide personalized recommendations based on scientific guidelines.
            </Typography>
          </Paper>
        </Grid>

        <Grid item xs={12} md={4}>
          <Paper elevation={3} sx={{ p: 3, height: '100%', display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
            <DataSaverOnIcon color="primary" sx={{ fontSize: 60, mb: 2 }} />
            <Typography variant="h6" gutterBottom align="center">
              Effortless Analysis
            </Typography>
            <Typography variant="body2" align="center">
              Simply upload an image of your fitness tracker data, and our AI does the rest. No manual data entry required.
            </Typography>
          </Paper>
        </Grid>

        <Grid item xs={12} md={4}>
          <Paper elevation={3} sx={{ p: 3, height: '100%', display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
            <VerifiedUserIcon color="primary" sx={{ fontSize: 60, mb: 2 }} />
            <Typography variant="h6" gutterBottom align="center">
              Privacy-Focused
            </Typography>
            <Typography variant="body2" align="center">
              Your data privacy is important to us. We process your images securely and don't store them permanently.
            </Typography>
          </Paper>
        </Grid>
      </Grid>

      <Paper elevation={3} sx={{ p: 4 }}>
        <Typography variant="h5" component="h2" gutterBottom>
          How It Works
        </Typography>
        <Typography variant="body1" paragraph>
          <strong>1. Upload:</strong> Submit an image of your fitness tracker summary.
        </Typography>
        <Typography variant="body1" paragraph>
          <strong>2. AI Analysis:</strong> Our AI extracts key metrics and analyzes them against health standards.
        </Typography>
        <Typography variant="body1" paragraph>
          <strong>3. Personalized Insights:</strong> Receive custom recommendations for activity, nutrition, and wellness.
        </Typography>
        <Typography variant="body1" paragraph>
          <strong>4. Track Progress:</strong> View your analysis history to monitor improvements over time.
        </Typography>
      </Paper>
    </Container>
  );
};

export default AboutPage;
