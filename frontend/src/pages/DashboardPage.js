import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import axios from 'axios';
import { 
  Container, 
  Typography, 
  Grid, 
  Paper, 
  Box, 
  Tabs, 
  Tab, 
  CircularProgress,
  Alert,
  Button
} from '@mui/material';
import { Bar } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from 'chart.js';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';

// Register Chart.js components
ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

const TabPanel = (props) => {
  const { children, value, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`simple-tabpanel-${index}`}
      aria-labelledby={`simple-tab-${index}`}
      {...other}
    >
      {value === index && (
        <Box sx={{ p: 3 }}>
          {children}
        </Box>
      )}
    </div>
  );
};

const DashboardPage = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [data, setData] = useState(null);
  const [tabValue, setTabValue] = useState(0);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(`/api/history/${id}`);
        setData(response.data);
      } catch (err) {
        setError('Failed to load analysis data. Please try again.');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [id]);

  const handleTabChange = (event, newValue) => {
    setTabValue(newValue);
  };

  const prepareChartData = () => {
    if (!data || !data.fitness_data) return null;
    
    // Filter numeric values for chart
    const chartData = {};
    Object.entries(data.fitness_data).forEach(([key, value]) => {
      if (typeof value === 'number') {
        chartData[key] = value;
      }
    });
    
    return {
      labels: Object.keys(chartData).map(key => key.replace('_', ' ').toUpperCase()),
      datasets: [
        {
          label: 'Fitness Metrics',
          data: Object.values(chartData),
          backgroundColor: 'rgba(75, 192, 192, 0.6)',
          borderColor: 'rgba(75, 192, 192, 1)',
          borderWidth: 1
        }
      ]
    };
  };

  if (loading) {
    return (
      <Container maxWidth="md" sx={{ textAlign: 'center', py: 8 }}>
        <CircularProgress />
        <Typography variant="h6" sx={{ mt: 2 }}>Loading your fitness analysis...</Typography>
      </Container>
    );
  }

  if (error || !data) {
    return (
      <Container maxWidth="md" sx={{ py: 4 }}>
        <Alert severity="error" sx={{ mb: 3 }}>{error || 'Analysis not found'}</Alert>
        <Button 
          variant="contained" 
          startIcon={<ArrowBackIcon />}
          onClick={() => navigate('/upload')}
        >
          Back to Upload
        </Button>
      </Container>
    );
  }

  const chartData = prepareChartData();

  return (
    <Container maxWidth="lg">
      <Button 
        startIcon={<ArrowBackIcon />} 
        sx={{ mb: 3 }}
        onClick={() => navigate(-1)}
      >
        Back
      </Button>
      
      <Typography variant="h4" component="h1" gutterBottom align="center">
        Your Health Dashboard
      </Typography>
      
      <Grid container spacing={4}>
        {/* Fitness Metrics */}
        <Grid item xs={12} md={6}>
          <Paper sx={{ p: 3 }}>
            <Typography variant="h5" gutterBottom>Your Fitness Metrics</Typography>
            <Box sx={{ mb: 3 }}>
              {Object.entries(data.fitness_data).map(([key, value]) => (
                <Box key={key} sx={{ display: 'flex', justifyContent: 'space-between', mb: 1 }}>
                  <Typography variant="body1" sx={{ textTransform: 'capitalize' }}>
                    {key.replace('_', ' ')}:
                  </Typography>
                  <Typography variant="body1" fontWeight="bold">
                    {value}
                  </Typography>
                </Box>
              ))}
            </Box>
            
            {chartData && (
              <Box sx={{ mt: 4 }}>
                <Bar data={chartData} />
              </Box>
            )}
          </Paper>
        </Grid>
        
        {/* Health Analysis */}
        <Grid item xs={12} md={6}>
          <Paper sx={{ p: 3 }}>
            <Typography variant="h5" gutterBottom>Health Analysis</Typography>
            {Object.entries(data.analysis_results).map(([key, value]) => {
              if (key === 'raw_data' || key === 'food_recommendations' || key === 'exercise_recommendations') {
                return null;
              }
              
              if (key === 'insights') {
                return (
                  <Box key={key} sx={{ mb: 3 }}>
                    <Typography variant="h6" sx={{ mb: 1, textTransform: 'capitalize' }}>
                      Health Insights
                    </Typography>
                    {value.map((insight, index) => (
                      <Typography key={index} variant="body1" sx={{ mb: 0.5 }}>
                        {insight}
                      </Typography>
                    ))}
                  </Box>
                );
              }
              
              return (
                <Box key={key} sx={{ mb: 2 }}>
                  <Typography variant="body1" sx={{ display: 'flex', justifyContent: 'space-between' }}>
                    <span style={{ textTransform: 'capitalize' }}>{key.replace(/_/g, ' ')}:</span>
                    <span style={{ fontWeight: 'bold' }}>{value}</span>
                  </Typography>
                </Box>
              );
            })}
          </Paper>
        </Grid>
      </Grid>
      
      {/* Recommendations */}
      <Paper sx={{ mt: 4 }}>
        <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
          <Tabs value={tabValue} onChange={handleTabChange} aria-label="recommendation tabs" centered>
            <Tab label="Activity" />
            <Tab label="Nutrition" />
            <Tab label="Wellness" />
          </Tabs>
        </Box>
        
        <TabPanel value={tabValue} index={0}>
          <Typography variant="h5" gutterBottom>Activity Recommendations</Typography>
          <div dangerouslySetInnerHTML={{ __html: data.recommendations.activity.replace(/\n/g, '<br/>') }} />
        </TabPanel>
        
        <TabPanel value={tabValue} index={1}>
          <Typography variant="h5" gutterBottom>Nutrition Recommendations</Typography>
          <div dangerouslySetInnerHTML={{ __html: data.recommendations.nutrition.replace(/\n/g, '<br/>') }} />
        </TabPanel>
        
        <TabPanel value={tabValue} index={2}>
          <Typography variant="h5" gutterBottom>Wellness Recommendations</Typography>
          <div dangerouslySetInnerHTML={{ __html: data.recommendations.wellness.replace(/\n/g, '<br/>') }} />
        </TabPanel>
      </Paper>
    </Container>
  );
};

export default DashboardPage;
