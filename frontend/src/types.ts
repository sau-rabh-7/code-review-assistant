export interface ReviewSuggestion {
    line: number;
    suggestion: string;
  }
  
  export interface ReportData {
    readability_score: number;
    modularity_score: number;
    bug_potential: number;
    overall_summary: string;
    suggestions: ReviewSuggestion[];
  }
  