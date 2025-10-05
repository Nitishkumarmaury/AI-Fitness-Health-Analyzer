import axios from 'axios';

// Create an axios instance with default config
const api = axios.create({
  baseURL: process.env.NODE_ENV === 'production' ? '' : 'http://localhost:5000',
  timeout: 60000, // Longer timeout for image processing
  headers: {
    'Content-Type': 'application/json',
  }
});

// Define API methods
export const analyzeImage = async (imageFile) => {
  try {
    const formData = new FormData();
    formData.append('image', imageFile);
    
    const response = await api.post('/api/analyze', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });
    
    return response.data;
  } catch (error) {
    console.error('Error analyzing image:', error);
    throw error.response?.data?.error || 'Error analyzing image. Please try again.';
  }
};

export const getHistory = async () => {
  try {
    const response = await api.get('/api/history');
    return response.data;
  } catch (error) {
    console.error('Error fetching history:', error);
    throw error.response?.data?.error || 'Error fetching history. Please try again.';
  }
};

export const getHistoryEntry = async (id) => {
  try {
    const response = await api.get(`/api/history/${id}`);
    return response.data;
  } catch (error) {
    console.error(`Error fetching history entry ${id}:`, error);
    throw error.response?.data?.error || 'Error fetching analysis details. Please try again.';
  }
};

export const getMetricsSummary = async () => {
  try {
    const response = await api.get('/api/metrics/summary');
    return response.data;
  } catch (error) {
    console.error('Error fetching metrics summary:', error);
    throw error.response?.data?.error || 'Error fetching metrics summary. Please try again.';
  }
};

export default api;
