import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { getHistoryEntry } from '../../utils/api';
import { useAppContext } from '../../context/AppContext';
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
  Button,
  Chip,
  Divider
} from '@mui/material';
import { 
  ArrowBack as ArrowBackIcon,
  CalendarToday as CalendarTodayIcon,
  DirectionsRun as DirectionsRunIcon,
  LocalFireDepartment as LocalFireDepartmentIcon
} from '@mui/icons-material';
import { Bar, Line } from 'react-chartjs-2';
import { 
  Chart as ChartJS, 
  CategoryScale, 
  LinearScale, 
  BarElement, 
  PointElement,
  LineElement,
  Title, 
  Tooltip, 
  Legend,
  Filler
} from 'chart.js';

// Register Chart.js components
ChartJS.register(
  CategoryScale, 
  LinearScale, 
  BarElement, 
  PointElement,
  LineElement,
  Title, 
  Tooltip, 
  Legend,
  Filler
);

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

const MetricCard = ({ title, value, unit, icon, color }) => (
  <Paper sx={{ p: 2, display: 'flex', alignItems: 'center', height: '100%' }}>
    <Box sx={{ 
      mr: 2, 
      p: 1.5, 
      borderRadius: '50%', 
      bgcolor: `${color}.light`,
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center'
    }}>
      {icon}
    </Box>
    <Box>
      <Typography variant="body2" color="text.secondary">
        {title}
      </Typography>
      <Typography variant="h5" component="div" fontWeight="bold">
        {value} {unit && <Typography component="span" variant="body2" color="text.secondary">{unit}</Typography>}
      </Typography>
    </Box>
  </Paper>
);

const DashboardPage = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const { history: appHistory, refreshData } = useAppContext();
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [data, setData] = useState(null);
  const [tabValue, setTabValue] = useState(0);
  const [trendData, setTrendData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      setLoading(true);
      try {
        const response = await getHistoryEntry(id);
        setData(response);
        
        // Find this entry in global history to calculate trends
        if (appHistory && appHistory.length > 0) {
          const currentIndex = appHistory.findIndex(item => item.id === parseInt(id));
          if (currentIndex !== -1 && currentIndex < appHistory.length - 1) {
            const previousEntry = appHistory[currentIndex + 1];
            prepareTrendData(response, previousEntry);
          }
        }
      } catch (err) {
        setError('Failed to load analysis data. Please try again.');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [id, appHistory]);

  const prepareTrendData = (current, previous) => {
    const trends = {};
    
    // Common metrics to compare
    const metrics = ['steps', 'calories', 'distance', 'active_minutes'];
    
    for (const metric of metrics) {
      const currentValue = current.fitness_data[metric] || current.fitness_data[`total_${metric}`];
      const previousValue = previous.fitness_data[metric] || previous.fitness_data[`total_${metric}`];
      
      if (currentValue !== undefined && previousValue !== undefined) {
        const change = currentValue - previousValue;
        const percentChange = (change / Math.abs(previousValue)) * 100;
        
        trends[metric] = {
          current: currentValue,
          previous: previousValue,
          change,
          percentChange: Math.round(percentChange),
          improved: change > 0
        };
      }
    }
    
    setTrendData(trends);
  };

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

  const formatDate = (dateString) => {
    try {
      return new Date(dateString).toLocaleString();
    } catch (error) {
      return dateString;
    }
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
    <Container maxWidth="lg" sx={{ py: 4 }}>
      <Box sx={{ display: 'flex', alignItems: 'center', mb: 4 }}>
        <Button 
          startIcon={<ArrowBackIcon />} 
          onClick={() => navigate(-1)}
          sx={{ mr: 2 }}
        >
          Back
        </Button>
        
        <Typography variant="h4" component="h1">
          Health Dashboard
        </Typography>
        
        <Box sx={{ ml: 'auto', display: 'flex', alignItems: 'center' }}>
          <CalendarTodayIcon fontSize="small" sx={{ mr: 1, color: 'text.secondary' }} />
          <Typography variant="body2" color="text.secondary">
            {formatDate(data.date)}
          </Typography>
        </Box>
      </Box>
      
      {/* Key Metrics Summary */}
      <Grid container spacing={3} sx={{ mb: 4 }}>
        <Grid item xs={12} sm={6} md={3}>
          <MetricCard 
            title="Steps" 
            value={data.fitness_data.steps || 0}
            icon={<DirectionsRunIcon sx={{ color: 'primary.main' }} />}
            color="primary"
          />
        </Grid>
        <Grid item xs={12} sm={6} md={3}>
          <MetricCard 
            title="Calories" 
            value={data.fitness_data.calories || data.fitness_data.total_calories || 0}
            unit="kcal"
            icon={<LocalFireDepartmentIcon sx={{ color: 'error.main' }} />}
            color="error"
          />
        </Grid>
        <Grid item xs={12} sm={6} md={3}>
          <MetricCard 
            title="Distance" 
            value={data.fitness_data.distance || 0}
            unit="km"
            icon={<DirectionsRunIcon sx={{ color: 'success.main' }} />}
            color="success"
          />
        </Grid>
        <Grid item xs={12} sm={6} md={3}>
          <MetricCard 
            title="Fitness Score" 
            value={data.analysis_results.fitness_score || 0}
            icon={<DirectionsRunIcon sx={{ color: 'warning.main' }} />}
            color="warning"
          />
        </Grid>
      </Grid>
      
      <Grid container spacing={4}>
        {/* Fitness Metrics */}
        <Grid item xs={12} md={6}>
          <Paper sx={{ p: 3 }}>
            <Typography variant="h6" gutterBottom>Your Fitness Metrics</Typography>
            
            {/* Metrics Table */}
            <Box sx={{ mb: 3 }}>
              {Object.entries(data.fitness_data).map(([key, value]) => (
                <Box 
                  key={key} 
                  sx={{ 
                    display: 'flex', 
                    justifyContent: 'space-between', 
                    mb: 1,
                    py: 1,
                    borderBottom: '1px solid',
                    borderColor: 'divider'
                  }}
                >
                  <Typography variant="body1" sx={{ textTransform: 'capitalize' }}>
                    {key.replace('_', ' ')}:
                  </Typography>
                  <Box sx={{ display: 'flex', alignItems: 'center' }}>
                    <Typography variant="body1" fontWeight="bold">
                      {value}
                    </Typography>
                    
                    {/* Show trend if available */}
                    {trendData && trendData[key] && (
                      <Chip 
                        size="small"
                        label={`${trendData[key].change > 0 ? '+' : ''}${trendData[key].change} (${trendData[key].percentChange}%)`}
                        color={trendData[key].improved ? 'success' : 'error'}
                        sx={{ ml: 1 }}
                      />
                    )}
                  </Box>
                </Box>
              ))}
            </Box>
            
            {/* Metrics Chart */}
            {chartData && (
              <Box sx={{ mt: 4 }}>
                <Typography variant="subtitle2" gutterBottom>Metrics Visualization</Typography>
                <Bar data={chartData} options={{
                  responsive: true,
                  maintainAspectRatio: true,
                  plugins: {
                    legend: {
                      display: false,
                    },
                    tooltip: {
                      backgroundColor: 'rgba(0, 0, 0, 0.8)',
                    }
                  }
                }} />
              </Box>
            )}
          </Paper>
        </Grid>
        
        {/* Health Analysis */}
        <Grid item xs={12} md={6}>
          <Paper sx={{ p: 3 }}>
            <Typography variant="h6" gutterBottom>Health Analysis</Typography>
            
            {/* Overall Fitness Score */}
            <Box sx={{ 
              mb: 3, 
              p: 2, 
              borderRadius: 1, 
              bgcolor: 'primary.light', 
              color: 'primary.contrastText',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between'
            }}>
              <Typography variant="subtitle1">Overall Fitness:</Typography>
              <Typography variant="h6">{data.analysis_results.overall_fitness || 'N/A'}</Typography>
            </Box>
            
            {/* Detailed Analysis */}
            {Object.entries(data.analysis_results).map(([key, value]) => {
              if (key === 'raw_data' || key === 'food_recommendations' || 
                  key === 'exercise_recommendations' || key === 'overall_fitness') {
                return null;
              }
              
              if (key === 'insights') {
                return (
                  <Box key={key} sx={{ mb: 3 }}>
                    <Typography variant="subtitle1" sx={{ mb: 1, fontWeight: 'bold' }}>
                      Health Insights
                    </Typography>
                    <Paper variant="outlined" sx={{ p: 2 }}>
                      {value.map((insight, index) => (
                        <Typography key={index} variant="body2" sx={{ mb: 1 }}>
                          {insight}
                        </Typography>
                      ))}
                    </Paper>
                  </Box>
                );
              }
              
              return (
                <Box key={key} sx={{ mb: 2 }}>
                  <Box sx={{ 
                    display: 'flex', 
                    justifyContent: 'space-between',
                    py: 1,
                    borderBottom: '1px solid',
                    borderColor: 'divider'
                  }}>
                    <Typography variant="body1" sx={{ textTransform: 'capitalize' }}>
                      {key.replace(/_/g, ' ')}:
                    </Typography>
                    <Typography variant="body1" fontWeight="bold">
                      {value}
                    </Typography>
                  </Box>
                </Box>
              );
            })}
          </Paper>
        </Grid>
      </Grid>
      
      {/* Recommendations */}
      <Paper sx={{ mt: 4 }}>
        <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
          <Tabs 
            value={tabValue} 
            onChange={handleTabChange} 
            aria-label="recommendation tabs" 
            centered
            indicatorColor="primary"
            textColor="primary"
          >
            <Tab label="Activity" />
            <Tab label="Nutrition" />
            <Tab label="Wellness" />
          </Tabs>
        </Box>
        
        <TabPanel value={tabValue} index={0}>
          <Typography variant="h6" gutterBottom>Activity Recommendations</Typography>
          <div className="markdown-content" dangerouslySetInnerHTML={{ 
            __html: data.recommendations.activity.replace(/\n/g, '<br/>').replace(/###\s(.*?)$/gm, '<h3>$1</h3>').replace(/- (.*?)$/gm, '<li>$1</li>') 
          }} />
        </TabPanel>
        
        <TabPanel value={tabValue} index={1}>
          <Typography variant="h6" gutterBottom>Nutrition Recommendations</Typography>
          <div className="markdown-content" dangerouslySetInnerHTML={{ 
            __html: data.recommendations.nutrition.replace(/\n/g, '<br/>').replace(/###\s(.*?)$/gm, '<h3>$1</h3>').replace(/- (.*?)$/gm, '<li>$1</li>') 
          }} />
        </TabPanel>
        
        <TabPanel value={tabValue} index={2}>
          <Typography variant="h6" gutterBottom>Wellness Recommendations</Typography>
          <div className="markdown-content" dangerouslySetInnerHTML={{ 
            __html: data.recommendations.wellness.replace(/\n/g, '<br/>').replace(/###\s(.*?)$/gm, '<h3>$1</h3>').replace(/- (.*?)$/gm, '<li>$1</li>') 
          }} />
        </TabPanel>
      </Paper>
      
      <Box sx={{ mt: 4, textAlign: 'center' }}>
        <Button 
          variant="contained" 
          color="primary" 
          onClick={() => navigate('/upload')}
          sx={{ mr: 2 }}
        >
          Analyze New Image
        </Button>
        <Button 
          variant="outlined" 
          onClick={() => {
            refreshData();
            navigate('/history');
          }}
        >
          View History
        </Button>
      </Box>
    </Container>
  );
};

export default DashboardPage;
