# Sales Data Processor

A simple Python project that processes sales data from a CSV file, generates a summary report, and creates a bar chart visualization.  

## Features
- Reads raw sales data from `data/sales.csv`
- Aggregates total sales by product
- Saves a summary report as `output/summary.csv`
- Generates a bar chart visualization as `output/sales_report.png`

## Project Structure
sales-data-processor/
├── data/ # Input data files
│   └── sales.csv
├── output/ # Generated reports (ignored by git)
│   ├── summary.csv
│   └── sales_report.png
├── src/ # Source code
│   └── main.py
├── requirements.txt # Python dependencies
├── .gitignore # Ignored files/folders
└── README.md # Project documentation

## Requirements
- Python 3.8+  
- Dependencies listed in `requirements.txt`

## Setup
Clone the repository and install dependencies:
```bash
git clone https://github.com/<your-username>/sales-data-processor.git
cd sales-data-processor

python3 -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows

pip install -r requirements.txt
Usage
Run the processor:
python src/main.py