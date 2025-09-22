import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import { 
  Container, 
  Typography, 
  Paper, 
  Box, 
  Button, 
  CircularProgress,
  Alert
} from '@mui/material';
import CloudUploadIcon from '@mui/icons-material/CloudUpload';
import ImageIcon from '@mui/icons-material/Image';
import ImageGuidelines from '../components/ImageGuidelines';

const UploadPage = () => {
  const navigate = useNavigate();
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (!selectedFile) return;
    
    setFile(selectedFile);
    setError('');
    
    // Create preview
    const reader = new FileReader();
    reader.onloadend = () => {
      setPreview(reader.result);
    };
    reader.readAsDataURL(selectedFile);
  };

  const handleDragOver = (e) => {
    e.preventDefault();
  };

  const handleDrop = (e) => {
    e.preventDefault();
    const selectedFile = e.dataTransfer.files[0];
    if (!selectedFile) return;
    
    // Check if the file is an image
    if (!selectedFile.type.startsWith('image/')) {
      setError('Please upload an image file (JPEG, PNG)');
      return;
    }
    
    setFile(selectedFile);
    setError('');
    
    // Create preview
    const reader = new FileReader();
    reader.onloadend = () => {
      setPreview(reader.result);
    };
    reader.readAsDataURL(selectedFile);
  };

  const handleSubmit = async () => {
    if (!file) {
      setError('Please select an image to upload');
      return;
    }
    
    // Check file size (max 10MB)
    if (file.size > 10 * 1024 * 1024) {
      setError('Image size too large. Please upload an image smaller than 10MB');
      return;
    }

    setLoading(true);
    setError('');
    
    const formData = new FormData();
    formData.append('image', file);
    
    try {
      const response = await axios.post('/api/analyze', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        },
        timeout: 60000 // Increase timeout to 60 seconds for large images
      });
      
      if (response.data && response.data.id) {
        navigate(`/dashboard/${response.data.id}`);
      } else {
        setError('Error processing the image. Please try another one.');
      }
    } catch (err) {
      console.error('Image analysis error:', err);
      
      // Provide more specific error messages based on the error
      if (err.response) {
        // Server responded with an error
        const serverError = err.response.data?.error || 'Unknown server error';
        setError(`Error: ${serverError}`);
      } else if (err.request) {
        // Request was made but no response received
        setError('Server not responding. Please check your internet connection and try again.');
      } else {
        // Error in setting up the request
        setError('Error analyzing the image. Please try a different image or format (JPEG/PNG).');
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <Container maxWidth="md">
      <Typography variant="h4" component="h1" gutterBottom align="center">
        Upload Fitness Data Image
      </Typography>
      
      <Typography variant="body1" paragraph align="center">
        Upload a screenshot of your fitness tracker summary to get personalized health insights and recommendations.
      </Typography>
      
      {error && (
        <Alert severity="error" sx={{ mb: 3 }}>{error}</Alert>
      )}
      
      <Paper 
        sx={{ 
          p: 3, 
          mb: 3, 
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          border: '2px dashed #ccc',
          borderRadius: 2,
          minHeight: 300,
          cursor: 'pointer'
        }}
        onDragOver={handleDragOver}
        onDrop={handleDrop}
        onClick={() => document.getElementById('file-input').click()}
      >
        <input
          id="file-input"
          type="file"
          accept="image/*"
          onChange={handleFileChange}
          style={{ display: 'none' }}
        />
        
        {preview ? (
          <Box sx={{ textAlign: 'center' }}>
            <img 
              src={preview} 
              alt="Preview" 
              style={{ maxWidth: '100%', maxHeight: 300, marginBottom: 16 }} 
            />
            <Typography variant="body2" color="text.secondary">
              {file?.name}
            </Typography>
          </Box>
        ) : (
          <Box sx={{ textAlign: 'center' }}>
            <ImageIcon sx={{ fontSize: 80, color: 'text.secondary', mb: 2 }} />
            <Typography variant="h6" gutterBottom>
              Drag & drop an image here or click to browse
            </Typography>
            <Typography variant="body2" color="text.secondary">
              Supported formats: JPEG, PNG
            </Typography>
          </Box>
        )}
      </Paper>
      
      <ImageGuidelines />
      
      <Box sx={{ textAlign: 'center' }}>
        <Button
          variant="contained"
          color="primary"
          size="large"
          startIcon={loading ? <CircularProgress size={24} color="inherit" /> : <CloudUploadIcon />}
          onClick={handleSubmit}
          disabled={!file || loading}
        >
          {loading ? 'Analyzing...' : 'Analyze Image'}
        </Button>
      </Box>
    </Container>
  );
};

export default UploadPage;
