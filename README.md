# Job Market Analyzer

## Project Overview
Job Market Analyzer is a Python-based application that analyzes job postings from a CSV dataset. It helps users explore job opportunities, search jobs by skills, visualize salary and location trends, generate reports, and compare resumes with job requirements.

## Features
- Load and analyze 220 job postings
- Search jobs by skill
- Display highest salary job
- Salary visualization using bar chart
- Top skills visualization
- Top job locations visualization
- Generate job market report
- AI Resume Matcher with match score and skill suggestions

## Technologies Used
- Python
- Pandas
- Matplotlib

## Project Structure
```
job-market-analyzer/
│
├── data/
│   └── jobs.csv
│
├── output/
│   └── report.txt
│
├── src/
│   ├── loader.py
│   ├── search.py
│   ├── chart.py
│   ├── analysis.py
│   ├── report.py
│   ├── location_chart.py
│   ├── ai_matcher.py
│   ├── models.py
│   └── sample_cv.txt
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Saloni-Joshi-codes/job-market-analyzer.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python main.py
```

## Menu Options

1. Show Total Jobs
2. Search Jobs by Skill
3. Salary Chart
4. Top Skills Chart
5. Highest Salary Job
6. Generate Report
7. Location Chart
8. AI Resume Matcher
9. Exit

## Author

**Saloni Joshi**

B.Tech CSE Student

IIT Jammu Summer School Capstone Project