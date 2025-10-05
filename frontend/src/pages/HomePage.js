import React from 'react';
import { useNavigate } from 'react-router-dom';
import { useAppContext } from '../context/AppContext';
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import Grid from '@mui/material/Grid';
import Paper from '@mui/material/Paper';
import Box from '@mui/material/Box';
// Remove unused import
// import FitnessCenterIcon from '@mui/icons-material/FitnessCenter';
import AssessmentIcon from '@mui/icons-material/Assessment';
import RecommendIcon from '@mui/icons-material/Recommend';
import InsightsIcon from '@mui/icons-material/Insights';
import UploadFileIcon from '@mui/icons-material/UploadFile';

const HomePage = () => {
  const navigate = useNavigate();
  const { history } = useAppContext();
  
  // Count analyzed images
  const analyzedCount = history?.length || 0;
  
  return (
    <Box>
      {/* Hero section */}
      <Box sx={{ 
        bgcolor: 'primary.main',
        color: 'white',
        py: 8,
        background: 'linear-gradient(135deg, #1976d2 0%, #42a5f5 100%)'
      }}>
        <Container maxWidth="md">
          <Typography 
            variant="h2" 
            component="h1" 
            gutterBottom 
            align="center" 
            sx={{ 
              fontWeight: 700
            }}
          >
            AI Fitness Health Analyzer
          </Typography>
          <Typography 
            variant="h5" 
            paragraph 
            align="center"
            sx={{ mb: 4 }}
          >
            Transform your fitness data into personalized health insights using AI
          </Typography>
          <Box sx={{ textAlign: 'center', mt: 4 }}>
            <Button 
              variant="contained" 
              color="secondary" 
              size="large"
              onClick={() => navigate('/upload')}
              startIcon={<UploadFileIcon />}
            >
              Upload Fitness Data
            </Button>
          </Box>
        </Container>
      </Box>

      {/* Features section */}
      <Container maxWidth="lg" sx={{ py: 8 }}>
        <Typography variant="h4" component="h2" gutterBottom align="center" sx={{ mb: 6 }}>
          How It Works
        </Typography>

        <Grid container spacing={4}>
          <Grid item xs={12} md={3}>
            <Paper elevation={3} sx={{ p: 3, height: '100%', display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
              <UploadFileIcon color="primary" sx={{ fontSize: 60, mb: 2 }} />
              <Typography variant="h6" gutterBottom align="center">
                Upload
              </Typography>
              <Typography variant="body1" align="center">
                Upload an image of your fitness tracker summary
              </Typography>
            </Paper>
          </Grid>

          <Grid item xs={12} md={3}>
            <Paper elevation={3} sx={{ p: 3, height: '100%', display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
              <AssessmentIcon color="primary" sx={{ fontSize: 60, mb: 2 }} />
              <Typography variant="h6" gutterBottom align="center">
                Extract
              </Typography>
              <Typography variant="body1" align="center">
                AI extracts fitness metrics like steps, calories, and distance
              </Typography>
            </Paper>
          </Grid>

          <Grid item xs={12} md={3}>
            <Paper elevation={3} sx={{ p: 3, height: '100%', display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
              <InsightsIcon color="primary" sx={{ fontSize: 60, mb: 2 }} />
              <Typography variant="h6" gutterBottom align="center">
                Analyze
              </Typography>
              <Typography variant="body1" align="center">
                Your data is analyzed to determine your fitness level and health status
              </Typography>
            </Paper>
          </Grid>

          <Grid item xs={12} md={3}>
            <Paper elevation={3} sx={{ p: 3, height: '100%', display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
              <RecommendIcon color="primary" sx={{ fontSize: 60, mb: 2 }} />
              <Typography variant="h6" gutterBottom align="center">
                Recommend
              </Typography>
              <Typography variant="body1" align="center">
                Receive personalized recommendations for exercise, nutrition, and wellness
              </Typography>
            </Paper>
          </Grid>
        </Grid>
      </Container>

      {/* CTA section */}
      <Box sx={{ bgcolor: 'grey.100', py: 8 }}>
        <Container maxWidth="md">
          <Typography variant="h4" component="h2" gutterBottom align="center">
            Ready to optimize your fitness journey?
          </Typography>
          <Typography variant="body1" paragraph align="center" sx={{ mb: 4 }}>
            Get started now and discover personalized insights based on your fitness data.
          </Typography>
          <Box sx={{ textAlign: 'center' }}>
            <Button 
              variant="contained" 
              color="primary" 
              size="large"
              onClick={() => navigate('/upload')}
            >
              Get Started
            </Button>
          </Box>
        </Container>
      </Box>
    </Box>
  );
};

export default HomePage;
