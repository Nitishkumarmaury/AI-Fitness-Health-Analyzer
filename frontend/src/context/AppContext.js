import React, { createContext, useState, useContext, useEffect } from 'react';
import { getHistory, getMetricsSummary } from '../utils/api';

// Create context
const AppContext = createContext();

// Context provider component
export const AppProvider = ({ children }) => {
  const [history, setHistory] = useState([]);
  const [metrics, setMetrics] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [lastRefresh, setLastRefresh] = useState(null);

  // Load history from API
  const loadHistory = async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await getHistory();
      setHistory(data);
      setLastRefresh(new Date());
    } catch (err) {
      setError(err.toString());
      console.error('Error loading history:', err);
    } finally {
      setLoading(false);
    }
  };

  // Load metrics summary
  const loadMetrics = async () => {
    try {
      const data = await getMetricsSummary();
      setMetrics(data);
    } catch (err) {
      console.error('Error loading metrics:', err);
      // Don't set error state here to avoid UI disruption
    }
  };

  // Refresh all data
  const refreshData = async () => {
    setLoading(true);
    try {
      await Promise.all([loadHistory(), loadMetrics()]);
    } finally {
      setLoading(false);
    }
  };

  // Load data on initial mount
  useEffect(() => {
    loadHistory();
    loadMetrics();
  }, []);

  // Create context value
  const contextValue = {
    history,
    metrics,
    loading,
    error,
    lastRefresh,
    refreshData,
    loadHistory,
    loadMetrics
  };

  return (
    <AppContext.Provider value={contextValue}>
      {children}
    </AppContext.Provider>
  );
};

// Custom hook for using the context
export const useAppContext = () => useContext(AppContext);

export default AppContext;
