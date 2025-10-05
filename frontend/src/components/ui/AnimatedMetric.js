import React from 'react';
import { Box, Typography, useTheme } from '@mui/material';
import { motion } from 'framer-motion';

const AnimatedMetric = ({ title, value, unit, icon, color = 'primary', delay = 0 }) => {
  const theme = useTheme();

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5, delay }}
    >
      <Box sx={{ 
        p: 2, 
        borderRadius: 2, 
        bgcolor: 'background.paper',
        boxShadow: 1,
        display: 'flex',
        alignItems: 'center',
        height: '100%'
      }}>
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
      </Box>
    </motion.div>
  );
};

export default AnimatedMetric;
