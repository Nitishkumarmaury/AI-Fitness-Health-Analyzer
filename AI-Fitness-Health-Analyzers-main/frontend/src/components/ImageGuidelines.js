import React from 'react';
import { Box, Typography, Paper, List, ListItem, ListItemIcon, ListItemText } from '@mui/material';
import CheckCircleOutlineIcon from '@mui/icons-material/CheckCircleOutline';
import CancelOutlinedIcon from '@mui/icons-material/CancelOutlined';

const ImageGuidelines = () => {
  return (
    <Paper sx={{ p: 3, mt: 3, mb: 3 }}>
      <Typography variant="h6" gutterBottom>
        Image Upload Guidelines
      </Typography>
      
      <Typography variant="body2" paragraph>
        For best results when analyzing fitness data, please follow these guidelines:
      </Typography>
      
      <Box sx={{ display: 'flex', flexDirection: { xs: 'column', md: 'row' }, gap: 2 }}>
        <Box sx={{ flex: 1 }}>
          <Typography variant="subtitle2" gutterBottom sx={{ color: 'success.main' }}>
            Recommended:
          </Typography>
          <List dense>
            <ListItem>
              <ListItemIcon sx={{ minWidth: 36 }}>
                <CheckCircleOutlineIcon color="success" fontSize="small" />
              </ListItemIcon>
              <ListItemText primary="Clear screenshots of fitness tracker summaries" />
            </ListItem>
            <ListItem>
              <ListItemIcon sx={{ minWidth: 36 }}>
                <CheckCircleOutlineIcon color="success" fontSize="small" />
              </ListItemIcon>
              <ListItemText primary="Images showing steps, calories, or distance data" />
            </ListItem>
            <ListItem>
              <ListItemIcon sx={{ minWidth: 36 }}>
                <CheckCircleOutlineIcon color="success" fontSize="small" />
              </ListItemIcon>
              <ListItemText primary="JPG or PNG formats" />
            </ListItem>
            <ListItem>
              <ListItemIcon sx={{ minWidth: 36 }}>
                <CheckCircleOutlineIcon color="success" fontSize="small" />
              </ListItemIcon>
              <ListItemText primary="Good lighting and resolution" />
            </ListItem>
          </List>
        </Box>
        
        <Box sx={{ flex: 1 }}>
          <Typography variant="subtitle2" gutterBottom sx={{ color: 'error.main' }}>
            Avoid:
          </Typography>
          <List dense>
            <ListItem>
              <ListItemIcon sx={{ minWidth: 36 }}>
                <CancelOutlinedIcon color="error" fontSize="small" />
              </ListItemIcon>
              <ListItemText primary="Blurry or low-quality images" />
            </ListItem>
            <ListItem>
              <ListItemIcon sx={{ minWidth: 36 }}>
                <CancelOutlinedIcon color="error" fontSize="small" />
              </ListItemIcon>
              <ListItemText primary="Images without clear fitness metrics" />
            </ListItem>
            <ListItem>
              <ListItemIcon sx={{ minWidth: 36 }}>
                <CancelOutlinedIcon color="error" fontSize="small" />
              </ListItemIcon>
              <ListItemText primary="Screenshots with sensitive personal information" />
            </ListItem>
            <ListItem>
              <ListItemIcon sx={{ minWidth: 36 }}>
                <CancelOutlinedIcon color="error" fontSize="small" />
              </ListItemIcon>
              <ListItemText primary="Very large files (keep under 10MB)" />
            </ListItem>
          </List>
        </Box>
      </Box>
    </Paper>
  );
};

export default ImageGuidelines;
