import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import { 
  Container, 
  Typography, 
  Paper,
  List, 
  ListItem, 
  ListItemText, 
  ListItemSecondaryAction, 
  IconButton, 
  Divider, 
  Button,
  CircularProgress,
  Alert
} from '@mui/material';
import ChevronRightIcon from '@mui/icons-material/ChevronRight';

const HistoryPage = () => {
  const navigate = useNavigate();
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchHistory = async () => {
      try {
        const response = await axios.get('/api/history');
        setHistory(response.data);
      } catch (err) {
        setError('Failed to load history. Please try again.');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchHistory();
  }, []);

  const formatDate = (dateString) => {
    try {
      return new Date(dateString).toLocaleString();
    } catch (error) {
      return dateString;
    }
  };

  const getSummary = (entry) => {
    const { fitness_data, analysis_results } = entry;
    let summary = '';
    
    if (fitness_data.steps) {
      summary += `${fitness_data.steps} steps`;
    }
    
    if (fitness_data.calories || fitness_data.total_calories) {
      summary += summary ? ', ' : '';
      summary += `${fitness_data.calories || fitness_data.total_calories} calories`;
    }
    
    if (analysis_results.activity_level) {
      summary += summary ? ' • ' : '';
      summary += `${analysis_results.activity_level}`;
    }
    
    return summary || 'No summary available';
  };

  const viewEntry = (id) => {
    navigate(`/dashboard/${id}`);
  };

  if (loading) {
    return (
      <Container maxWidth="md" sx={{ textAlign: 'center', py: 8 }}>
        <CircularProgress />
        <Typography variant="h6" sx={{ mt: 2 }}>Loading your history...</Typography>
      </Container>
    );
  }

  return (
    <Container maxWidth="md">
      <Typography variant="h4" component="h1" gutterBottom align="center">
        Your Analysis History
      </Typography>
      
      {error && (
        <Alert severity="error" sx={{ mb: 3 }}>{error}</Alert>
      )}
      
      {history.length === 0 ? (
        <Paper sx={{ p: 4, textAlign: 'center' }}>
          <Typography variant="h6" gutterBottom>No history available yet</Typography>
          <Typography variant="body1" paragraph>
            Start analyzing your fitness data to build your history.
          </Typography>
          <Button 
            variant="contained" 
            color="primary"
            onClick={() => navigate('/upload')}
          >
            Upload Fitness Data
          </Button>
        </Paper>
      ) : (
        <Paper>
          <List>
            {history.slice().reverse().map((entry, index) => (
              <React.Fragment key={entry.id}>
                <ListItem button onClick={() => viewEntry(entry.id)}>
                  <ListItemText 
                    primary={formatDate(entry.date)}
                    secondary={getSummary(entry)}
                  />
                  <ListItemSecondaryAction>
                    <IconButton edge="end" onClick={() => viewEntry(entry.id)}>
                      <ChevronRightIcon />
                    </IconButton>
                  </ListItemSecondaryAction>
                </ListItem>
                {index < history.length - 1 && <Divider />}
              </React.Fragment>
            ))}
          </List>
        </Paper>
      )}
    </Container>
  );
};


export default HistoryPage;
