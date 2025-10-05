import { createTheme } from '@mui/material/styles';

const theme = createTheme({
  palette: {
    primary: {
      main: '#6C63FF', // Vibrant purple
      light: '#A084E8',
      dark: '#3D348B',
      contrastText: '#fff',
    },
    secondary: {
      main: '#FF6584', // Playful pink
      light: '#FFD86E',
      dark: '#FF4F5A',
      contrastText: '#fff',
    },
    accent: {
      main: '#FFD86E', // Yellow accent
    },
    success: {
      main: '#43E97B',
      light: '#38F9D7',
    },
    warning: {
      main: '#FFD86E',
    },
    error: {
      main: '#FF4F5A',
    },
    background: {
      default: 'linear-gradient(135deg, #F9F9F9 0%, #E0C3FC 100%)',
      paper: '#fff',
    },
    info: {
      main: '#38F9D7',
    },
    text: {
      primary: '#3D348B',
      secondary: '#6C63FF',
    },
  },
  typography: {
    fontFamily: 'Poppins, Roboto, Helvetica, Arial, sans-serif',
    h1: {
      fontSize: '2.8rem',
      fontWeight: 700,
      color: '#6C63FF',
    },
    h2: {
      fontSize: '2.2rem',
      fontWeight: 600,
      color: '#FF6584',
    },
    h3: {
      fontSize: '1.8rem',
      fontWeight: 600,
      color: '#3D348B',
    },
    h4: {
      fontSize: '1.5rem',
      fontWeight: 600,
      color: '#A084E8',
    },
    h5: {
      fontSize: '1.25rem',
      fontWeight: 500,
    },
    h6: {
      fontSize: '1.1rem',
      fontWeight: 500,
    },
  },
  shape: {
    borderRadius: 16,
  },
  components: {
    MuiButton: {
      styleOverrides: {
        root: {
          borderRadius: 16,
          textTransform: 'none',
          fontSize: '1.05rem',
          fontWeight: 600,
          boxShadow: '0 4px 16px rgba(255,101,132,0.10)',
          background: 'linear-gradient(90deg, #6C63FF 0%, #FF6584 100%)',
          color: '#fff',
        },
      },
    },
    MuiCard: {
      styleOverrides: {
        root: {
          borderRadius: 24,
          boxShadow: '0 6px 24px rgba(255,101,132,0.10)',
          background: 'linear-gradient(135deg, #E0C3FC 0%, #FFD86E 100%)',
        },
      },
    },
    MuiAppBar: {
      styleOverrides: {
        root: {
          background: 'linear-gradient(90deg, #6C63FF 0%, #FF6584 100%)',
        },
      },
    },
    MuiPaper: {
      styleOverrides: {
        root: {
          borderRadius: 16,
        },
      },
    },
  },
});

export default theme;
