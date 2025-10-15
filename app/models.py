from pydantic import BaseModel, Field
from typing import List

class CodeInput(BaseModel):
    """Defines the structure for the code submission."""
    language: str = Field(..., example="python", description="The programming language of the code.")
    code: str = Field(..., example="def my_func(a,b):\n  return a+b", description="The source code to be reviewed.")

class ReviewSuggestion(BaseModel):
    """Defines the structure for a single improvement suggestion."""
    line: int = Field(..., example=5, description="The line number the suggestion applies to.")
    suggestion: str = Field(..., example="Variable 'x' is not descriptive. Consider renaming to 'user_count'.")

class CodeReviewReport(BaseModel):
    """Defines the structure for the final review report."""
    readability_score: float = Field(..., ge=1.0, le=10.0, description="Score from 1-10 indicating code readability.")
    modularity_score: float = Field(..., ge=1.0, le=10.0, description="Score from 1-10 indicating code modularity.")
    bug_potential: float = Field(..., ge=1.0, le=10.0, description="Score from 1-10 indicating the likelihood of bugs (10 is high potential).")
    overall_summary: str = Field(..., description="A brief summary of the code's quality.")
    suggestions: List[ReviewSuggestion] = Field(..., description="A list of specific, actionable suggestions for improvement.")