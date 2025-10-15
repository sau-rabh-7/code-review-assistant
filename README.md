# Code Review Assistant 🤖

## Objective
An automated code review assistant that analyzes source code files for structure, readability, and best practices using Large Language Model (LLM) integration. This project provides a backend API to submit code and receive a detailed review report.

## Features
- **RESTful API**: A clean, documented API built with FastAPI.
- **LLM Integration**: Leverages an LLM to provide insightful analysis of code quality.
- **Structured Reports**: Delivers review reports in a consistent JSON format, including:
  - Quantitative scores (readability, modularity, bug potential).
  - A qualitative summary.
  - Actionable, line-specific suggestions.
- **Language Agnostic**: Can accept code from any programming language supported by the underlying LLM.

## Technical Stack
- **Backend**: Python 3.10+
- **Framework**: FastAPI
- **Server**: Uvicorn
- **Data Validation**: Pydantic

## Setup and Installation

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd code-review-assistant
```

### 2. Create a virtual environment and activate it
```bash
# For Unix/macOS
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

## How to Run the API Server

Run the Uvicorn server from the root directory of the project:
```bash
uvicorn app.main:app --reload
```
The API will be available at `http://127.0.0.1:8000`.

## API Usage

You can access the interactive API documentation (powered by Swagger UI) by navigating to:
**`http://127.0.0.1:8000/docs`**

### Example Request (`curl`)

You can also interact with the API using a tool like `curl`.

```bash
curl -X 'POST' \
  '[http://127.0.0.1:8000/review](http://127.0.0.1:8000/review)' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "language": "python",
    "code": "def process_data(data):\n  d = data\n  result = []\n  for x in d:\n    details = x[\"details\"]\n    if details[\"value\"] > 10:\n      result.append(x)\n  return result"
  }'
```

### Example Response

```json
{
  "readability_score": 5.5,
  "modularity_score": 4,
  "bug_potential": 7,
  "overall_summary": "The code works but lacks modularity and uses non-descriptive variable names. There is a potential for a runtime error if dictionary keys are missing.",
  "suggestions": [
    {
      "line": 2,
      "suggestion": "Variable 'd' is not descriptive. Consider renaming to 'data_list' or something more specific to its content."
    },
    {
      "line": 4,
      "suggestion": "The variable 'x' is vague. Rename it to 'item' or 'record' for clarity."
    },
    {
      "line": 5,
      "suggestion": "Potential 'KeyError' if 'details' does not exist in an item. Use `x.get('details', {})` for safer access."
    },
    {
      "line": 6,
      "suggestion": "This complex logic could be extracted into its own function to improve the modularity of `process_data`."
    }
  ]
}
```

## Future Improvements
- **Real LLM Integration**: Replace the simulated LLM call in `app/llm_analyzer.py` with an actual API call to a provider like OpenAI or Google AI.
- **Database Integration**: Add a database (e.g., PostgreSQL with SQLAlchemy) to store historical review reports.
- **Web Dashboard**: Build a simple frontend (e.g., using React or Vue.js) to allow users to upload files and view reports in a user-friendly interface.
- **Authentication**: Implement user authentication to secure the API and associate reports with users.