import React from 'react';
import { Card, CardContent, Typography, Box, Chip } from '@mui/material';

const AnalysisCard = ({ title, value, description, color = 'primary', trend }) => {
  return (
    <Card sx={{ 
      height: '100%',
      transition: 'transform 0.2s, box-shadow 0.2s',
      '&:hover': {
        transform: 'translateY(-2px)',
        boxShadow: 4
      }
    }}>
      <CardContent>
        <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', mb: 2 }}>
          <Typography variant="h6" component="h3" color="text.secondary">
            {title}
          </Typography>
          {trend && (
            <Chip 
              size="small"
              label={`${trend > 0 ? '+' : ''}${trend}%`}
              color={trend > 0 ? 'success' : 'error'}
            />
          )}
        </Box>
        
        <Typography variant="h4" component="div" color={`${color}.main`} sx={{ mb: 1 }}>
          {value}
        </Typography>
        
        {description && (
          <Typography variant="body2" color="text.secondary">
            {description}
          </Typography>
        )}
      </CardContent>
    </Card>
  );
};

export default AnalysisCard;
