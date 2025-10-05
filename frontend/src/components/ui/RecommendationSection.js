import React from 'react';
import { Paper, Typography, Box, List, ListItem, ListItemText, Divider } from '@mui/material';

const RecommendationSection = ({ title, recommendations, icon }) => {
  const parseRecommendations = (text) => {
    if (!text) return [];
    
    // Split by lines and filter out empty ones
    const lines = text.split('\n').filter(line => line.trim());
    
    // Look for bullet points or numbered items
    const items = lines.filter(line => 
      line.trim().startsWith('-') || 
      line.trim().startsWith('•') || 
      /^\d+\./.test(line.trim())
    );
    
    return items.length > 0 ? items : [text];
  };

  const items = parseRecommendations(recommendations);

  return (
    <Paper sx={{ p: 3 }}>
      <Box sx={{ display: 'flex', alignItems: 'center', mb: 2 }}>
        {icon && (
          <Box sx={{ mr: 2, color: 'primary.main' }}>
            {icon}
          </Box>
        )}
        <Typography variant="h6" component="h3">
          {title}
        </Typography>
      </Box>
      
      <Divider sx={{ mb: 2 }} />
      
      {items.length > 1 ? (
        <List>
          {items.map((item, index) => (
            <ListItem key={index} sx={{ px: 0 }}>
              <ListItemText 
                primary={item.replace(/^[-•\d\.]\s*/, '')}
                primaryTypographyProps={{ variant: 'body2' }}
              />
            </ListItem>
          ))}
        </List>
      ) : (
        <Typography variant="body2" sx={{ whiteSpace: 'pre-line' }}>
          {recommendations}
        </Typography>
      )}
    </Paper>
  );
};

export default RecommendationSection;
