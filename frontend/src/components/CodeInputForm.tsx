import { useState } from 'react';
import { TextField, Button, Box, FormControl, InputLabel, Select, MenuItem, Paper } from '@mui/material';

interface Props {
  onReview: (code: string, language: string) => void;
  isLoading: boolean;
}

const CodeInputForm = ({ onReview, isLoading }: Props) => {
  const [code, setCode] = useState('');
  const [language, setLanguage] = useState('python');

  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault();
    onReview(code, language);
  };

  return (
    <Paper elevation={3} sx={{ p: 3 }}>
      <form onSubmit={handleSubmit}>
        <FormControl fullWidth sx={{ mb: 2 }}>
          <InputLabel id="language-select-label">Language</InputLabel>
          <Select
            labelId="language-select-label"
            value={language}
            label="Language"
            onChange={(e) => setLanguage(e.target.value)}
          >
            <MenuItem value="python">Python</MenuItem>
            <MenuItem value="javascript">JavaScript</MenuItem>
            <MenuItem value="typescript">TypeScript</MenuItem>
            <MenuItem value="java">Java</MenuItem>
            <MenuItem value="csharp">C#</MenuItem>
            <MenuItem value="go">Go</MenuItem>
          </Select>
        </FormControl>
        <TextField
          label="Paste your code here..."
          multiline
          rows={15}
          value={code}
          onChange={(e) => setCode(e.target.value)}
          fullWidth
          variant="outlined"
          sx={{ mb: 2, fontFamily: 'monospace' }}
        />
        <Button
          type="submit"
          variant="contained"
          size="large"
          disabled={isLoading || !code.trim()}
          fullWidth
        >
          {isLoading ? 'Analyzing...' : 'Review My Code'}
        </Button>
      </form>
    </Paper>
  );
};

export default CodeInputForm;