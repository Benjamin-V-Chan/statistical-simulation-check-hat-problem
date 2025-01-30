# statistical-simulation-check-hat-problem

## Project Overview

This project simulates the **Check-Hat Problem**, a well-known probability problem that examines the likelihood of individuals randomly picking their own hats from a collection. The statistical simulation helps analyze the expected number of correct matches and the probability distribution of the number of correct hat assignments.

## Folder Structure
```
project-root/
├── scripts/
│   ├── 01_simulation.py  # Runs the check-hat problem simulation for N trials
│   ├── 02_analysis.py     # Analyzes the simulation results
│   ├── 03_visualization.py # Generates plots and summary statistics
│   ├── utils.py           # Helper functions for modularity
├── outputs/               # Stores output data and results
│   ├── simulation_results.csv
│   ├── analysis_summary.txt
│   ├── visualizations/
│       ├── histogram.png
│       ├── probability_curve.png
├── README.md              # Documentation
├── requirements.txt        # Dependencies
```

## Usage

### 1. Setup the Project:
Clone the repository. Ensure you have Python installed. Install required dependencies using the requirements.txt file:
```bash
pip install -r requirements.txt
```

### 2. Run the Simulation:
Execute the simulation script to generate results:
```bash
python scripts/01_simulation.py
```
This will create an output file `outputs/simulation_results.csv` containing the number of correct matches for each trial.

### 3. Run the Analysis:
To compute summary statistics and probability estimates, run:
```bash
python scripts/02_analysis.py
```
This will generate an `outputs/analysis_summary.txt` file with key insights, including:
- Mean number of correct matches
- Variance of matches
- Probability of at least one correct match

### 4. Generate Visualizations:
Create a histogram and probability curve for the simulation results:
```bash
python scripts/03_visualization.py
```
Resulting plots are saved in `outputs/visualizations/`.

## Requirements
The following Python packages are required:
```txt
numpy
matplotlib
csv
```
These can be installed via `pip install -r requirements.txt`