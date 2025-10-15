import { useState } from 'react';
import { Container, Typography, createTheme, ThemeProvider, CssBaseline, Box, CircularProgress, Alert } from '@mui/material';
import CodeInputForm from './components/CodeInputForm';
import ReviewReport from './components/ReviewReport';
import axios from 'axios';
import type { ReportData } from './types';

// export interface ReviewSuggestion {
//   line: number;
//   suggestion: string;
// }

// export interface ReportData {
//   readability_score: number;
//   modularity_score: number;
//   bug_potential: number;
//   overall_summary: string;
//   suggestions: ReviewSuggestion[];
// }

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
});

function App() {
  const [report, setReport] = useState<ReportData | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleReviewRequest = async (code: string, language: string) => {
    setIsLoading(true);
    setError(null);
    setReport(null);

    try {
      const response = await axios.post('http://127.0.0.1:8000/review', {
        language,
        code,
      });
      setReport(response.data);
    } catch (err: any) {
      setError(err.response?.data?.detail || 'An unexpected error occurred.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <ThemeProvider theme={darkTheme}>
      <CssBaseline />
      <Container maxWidth="lg" sx={{ py: 4 }}>
        <Typography variant="h3" component="h1" align="center" gutterBottom>
          🤖 AI Code Review Assistant
        </Typography>
        <Typography align="center" color="text.secondary" sx={{ mb: 4 }}>
          Paste your code, select the language, and get an instant analysis from an AI expert.
        </Typography>
        
        <CodeInputForm onReview={handleReviewRequest} isLoading={isLoading} />
        
        <Box sx={{ mt: 4 }}>
          {isLoading && (
            <Box sx={{ display: 'flex', justifyContent: 'center', my: 4 }}>
              <CircularProgress />
            </Box>
          )}
          {error && <Alert severity="error">{error}</Alert>}
          {report && <ReviewReport report={report} />}
        </Box>
      </Container>
    </ThemeProvider>
  );
}

export default App;