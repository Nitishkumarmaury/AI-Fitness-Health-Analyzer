import React from 'react';
import { useNavigate } from 'react-router-dom';
import { useAppContext } from '../../context/AppContext';
import { 
  Container, 
  Typography, 
  Button, 
  Grid, 
  Paper, 
  Box,
  Card,
  CardContent,
  CardMedia,
  List,
  ListItem,
  ListItemIcon,
  ListItemText,
  Divider
} from '@mui/material';
import {
  UploadFile as UploadFileIcon,
  Assessment as AssessmentIcon,
  Recommend as RecommendIcon,
  Insights as InsightsIcon,
  Check as CheckIcon,
  ArrowForward as ArrowForwardIcon
} from '@mui/icons-material';
import fitnessBackground from '../../assets/fitness-bg.jpg';

// Feature item component
const FeatureItem = ({ icon, title, description }) => (
  <Grid item xs={12} md={4}>
    <Paper elevation={3} sx={{ 
      p: 3, 
      height: '100%', 
      display: 'flex', 
      flexDirection: 'column', 
      alignItems: 'center',
      transition: 'transform 0.3s, box-shadow 0.3s',
      '&:hover': {
        transform: 'translateY(-5px)',
        boxShadow: 6
      }
    }}>
      {icon}
      <Typography variant="h6" gutterBottom align="center" sx={{ mt: 2 }}>
        {title}
      </Typography>
      <Typography variant="body2" align="center">
        {description}
      </Typography>
    </Paper>
  </Grid>
);

// Benefit item component
const BenefitItem = ({ text }) => (
  <ListItem>
    <ListItemIcon>
      <CheckIcon color="primary" />
    </ListItemIcon>
    <ListItemText primary={text} />
  </ListItem>
);

const HomePage = () => {
  const navigate = useNavigate();
  const { history } = useAppContext();
  
  // Count analyzed images
  const analyzedCount = history?.length || 0;
  
  return (
    <Box>
      {/* Hero section */}
      <Box sx={{ 
        position: 'relative',
        height: '500px', 
        display: 'flex',
        alignItems: 'center',
        overflow: 'hidden',
        mb: 6
      }}>
        {/* Background image with overlay */}
        <Box sx={{
          position: 'absolute',
          top: 0,
          left: 0,
          width: '100%',
          height: '100%',
          zIndex: -1,
          '&::before': {
            content: '""',
            position: 'absolute',
            top: 0,
            left: 0,
            width: '100%',
            height: '100%',
            backgroundColor: 'rgba(0, 0, 0, 0.6)',
            zIndex: 1
          }
        }}>
          <Box 
            component="img"
            src={fitnessBackground}
            alt="Fitness"
            sx={{
              width: '100%',
              height: '100%',
              objectFit: 'cover'
            }}
          />
        </Box>
        
        <Container maxWidth="md" sx={{ position: 'relative', zIndex: 2 }}>
          <Typography 
            variant="h2" 
            component="h1" 
            gutterBottom 
            align="center" 
            sx={{ 
              color: 'white',
              fontWeight: 700,
              textShadow: '2px 2px 4px rgba(0,0,0,0.5)'
            }}
          >
            AI Fitness Health Analyzer
          </Typography>
          <Typography 
            variant="h5" 
            paragraph 
            align="center"
            sx={{ 
              color: 'white',
              mb: 4,
              textShadow: '1px 1px 2px rgba(0,0,0,0.5)'
            }}
          >
            Transform your fitness data into personalized health insights using AI
          </Typography>
          <Box sx={{ textAlign: 'center', mt: 4 }}>
            <Button 
              variant="contained" 
              color="primary" 
              size="large"
              onClick={() => navigate('/upload')}
              startIcon={<UploadFileIcon />}
              sx={{ 
                py: 1.5, 
                px: 4, 
                fontSize: '1.1rem',
                boxShadow: 3,
                '&:hover': {
                  boxShadow: 5
                }
              }}
            >
              Upload Fitness Data
            </Button>
            
            {analyzedCount > 0 && (
              <Button 
                variant="outlined"
                color="secondary" 
                size="large"
                onClick={() => navigate('/history')}
                startIcon={<InsightsIcon />}
                sx={{ 
                  py: 1.5, 
                  px: 4, 
                  fontSize: '1.1rem',
                  ml: 2,
                  backgroundColor: 'rgba(255,255,255,0.1)',
                  color: 'white',
                  borderColor: 'white',
                  '&:hover': {
                    backgroundColor: 'rgba(255,255,255,0.2)',
                    borderColor: 'white'
                  }
                }}
              >
                View History
              </Button>
            )}
          </Box>
        </Container>
      </Box>

      {/* Features section */}
      <Container maxWidth="lg" sx={{ py: 8 }}>
        <Typography variant="h4" component="h2" gutterBottom align="center" sx={{ mb: 6 }}>
          How It Works
        </Typography>

        <Grid container spacing={4}>
          <FeatureItem 
            icon={<UploadFileIcon color="primary" sx={{ fontSize: 60 }} />}
            title="Upload"
            description="Upload an image of your fitness tracker summary from any device or app"
          />

          <FeatureItem 
            icon={<AssessmentIcon color="primary" sx={{ fontSize: 60 }} />}
            title="Extract & Analyze"
            description="Our AI extracts key metrics and analyzes them against health standards"
          />

          <FeatureItem 
            icon={<RecommendIcon color="primary" sx={{ fontSize: 60 }} />}
            title="Get Recommendations"
            description="Receive personalized recommendations for activity, nutrition, and wellness"
          />
        </Grid>
      </Container>

      {/* Benefits section */}
      <Box sx={{ bgcolor: 'grey.100', py: 8 }}>
        <Container maxWidth="lg">
          <Grid container spacing={6} alignItems="center">
            <Grid item xs={12} md={6}>
              <Typography variant="h4" component="h2" gutterBottom>
                Why Use AI Fitness Health Analyzer?
              </Typography>
              
              <Typography variant="body1" paragraph sx={{ mb: 4 }}>
                Our advanced AI technology provides personalized insights based on your specific fitness data,
                helping you make informed decisions about your health journey.
              </Typography>
              
              <List>
                <BenefitItem text="Get personalized recommendations tailored to your activity level" />
                <BenefitItem text="Track your progress and see improvements over time" />
                <BenefitItem text="Understand your fitness metrics in context with expert analysis" />
                <BenefitItem text="Receive actionable advice for improving your health" />
                <BenefitItem text="Privacy-focused processing - your data remains secure" />
              </List>
              
              <Button 
                variant="contained" 
                color="primary"
                size="large"
                endIcon={<ArrowForwardIcon />}
                onClick={() => navigate('/upload')}
                sx={{ mt: 2 }}
              >
                Get Started Now
              </Button>
            </Grid>
            
            <Grid item xs={12} md={6}>
              <Card sx={{ 
                maxWidth: 500, 
                mx: 'auto',
                boxShadow: 3,
                overflow: 'hidden',
                borderRadius: 2
              }}>
                <CardMedia
                  component="img"
                  height="300"
                  image="/fitness-app-screenshot.jpg"
                  alt="Fitness App"
                  sx={{ objectFit: 'cover' }}
                />
                <CardContent sx={{ p: 3 }}>
                  <Typography gutterBottom variant="h5" component="div">
                    Powered by Google Gemini AI
                  </Typography>
                  <Typography variant="body2" color="text.secondary">
                    Our application leverages Google's advanced Gemini 1.5-flash AI model to extract and
                    analyze fitness data with high accuracy, providing you with reliable insights.
                  </Typography>
                </CardContent>
              </Card>
            </Grid>
          </Grid>
        </Container>
      </Box>

      {/* CTA section */}
      <Box sx={{ bgcolor: 'primary.main', color: 'white', py: 8 }}>
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
              color="secondary" 
              size="large"
              onClick={() => navigate('/upload')}
              sx={{ 
                py: 1.5, 
                px: 4, 
                fontSize: '1.1rem',
                boxShadow: 3
              }}
            >
              Analyze Your Fitness Data
            </Button>
          </Box>
        </Container>
      </Box>
    </Box>
  );
};

export default HomePage;
