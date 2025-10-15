import { Box, Typography, Paper, Grid, Card, CardContent, Divider, List, ListItem, ListItemIcon, ListItemText } from '@mui/material';
import type { ReportData } from '../types';
import CodeIcon from '@mui/icons-material/Code';

interface Props {
  report: ReportData;
}

const ScoreCard = ({ title, value, tooltip }: { title: string; value: number; tooltip: string }) => (
  <Card sx={{ textAlign: 'center', height: '100%' }}>
    <CardContent>
      <Typography variant="h2" color="primary">{value.toFixed(1)}</Typography>
      <Typography variant="h6" component="div">{title}</Typography>
      <Typography variant="body2" color="text.secondary">{tooltip}</Typography>
    </CardContent>
  </Card>
);

const ReviewReport = ({ report }: Props) => {
  return (
    <Paper elevation={3} sx={{ p: 4 }}>
      <Typography variant="h4" gutterBottom>Review Report</Typography>
      
      <Grid container spacing={3} sx={{ my: 2 }}>
        <Grid item xs={12} md={4}>
          <ScoreCard title="Readability" value={report.readability_score} tooltip="1 (low) to 10 (high)" />
        </Grid>
        <Grid item xs={12} md={4}>
          <ScoreCard title="Modularity" value={report.modularity_score} tooltip="1 (low) to 10 (high)" />
        </Grid>
        <Grid item xs={12} md={4}>
          <ScoreCard title="Bug Potential" value={report.bug_potential} tooltip="1 (low) to 10 (high)" />
        </Grid>
      </Grid>

      <Box sx={{ my: 3 }}>
        <Typography variant="h5" gutterBottom>Overall Summary</Typography>
        <Typography variant="body1" sx={{ fontStyle: 'italic', color: 'text.secondary' }}>
          "{report.overall_summary}"
        </Typography>
      </Box>

      <Divider sx={{ my: 3 }} />

      <Typography variant="h5" gutterBottom>Actionable Suggestions</Typography>
      <List>
        {report.suggestions.map((item, index) => (
          <ListItem key={index} alignItems="flex-start">
            <ListItemIcon>
              <CodeIcon color="primary" />
            </ListItemIcon>
            <ListItemText
              primary={`Line ${item.line}:`}
              secondary={item.suggestion}
            />
          </ListItem>
        ))}
      </List>
    </Paper>
  );
};

export default ReviewReport;