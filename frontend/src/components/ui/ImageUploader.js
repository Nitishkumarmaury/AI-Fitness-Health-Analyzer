import React, { useState, useCallback } from 'react';
import { Box, Typography, Paper, Button } from '@mui/material';
import { useDropzone } from 'react-dropzone';
import CloudUploadIcon from '@mui/icons-material/CloudUpload';
import ImageIcon from '@mui/icons-material/Image';

const ImageUploader = ({ onImageUpload, accept = 'image/*', maxSize = 10485760 }) => {
  const [preview, setPreview] = useState(null);
  const [error, setError] = useState('');

  const onDrop = useCallback((acceptedFiles, rejectedFiles) => {
    setError('');
    
    if (rejectedFiles.length > 0) {
      setError('Please upload a valid image file under 10MB');
      return;
    }

    const file = acceptedFiles[0];
    if (file) {
      // Create preview
      const reader = new FileReader();
      reader.onloadend = () => {
        setPreview(reader.result);
      };
      reader.readAsDataURL(file);
      
      // Call parent callback
      onImageUpload(file);
    }
  }, [onImageUpload]);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: { 'image/*': ['.jpeg', '.jpg', '.png'] },
    maxSize,
    multiple: false
  });

  return (
    <Paper 
      {...getRootProps()}
      sx={{ 
        p: 3, 
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        border: '2px dashed',
        borderColor: isDragActive ? 'primary.main' : 'grey.400',
        borderRadius: 2,
        minHeight: 300,
        cursor: 'pointer',
        transition: 'border-color 0.3s',
        '&:hover': {
          borderColor: 'primary.main'
        }
      }}
    >
      <input {...getInputProps()} />
      
      {preview ? (
        <Box sx={{ textAlign: 'center' }}>
          <img 
            src={preview} 
            alt="Preview" 
            style={{ maxWidth: '100%', maxHeight: 300, marginBottom: 16 }} 
          />
          <Typography variant="body2" color="text.secondary">
            Click or drag to replace image
          </Typography>
        </Box>
      ) : (
        <Box sx={{ textAlign: 'center' }}>
          <ImageIcon sx={{ fontSize: 80, color: 'text.secondary', mb: 2 }} />
          <Typography variant="h6" gutterBottom>
            {isDragActive ? 'Drop image here' : 'Drag & drop an image here or click to browse'}
          </Typography>
          <Typography variant="body2" color="text.secondary">
            Supported formats: JPEG, PNG (Max size: 10MB)
          </Typography>
        </Box>
      )}
      
      {error && (
        <Typography variant="body2" color="error" sx={{ mt: 2 }}>
          {error}
        </Typography>
      )}
    </Paper>
  );
};

export default ImageUploader;
