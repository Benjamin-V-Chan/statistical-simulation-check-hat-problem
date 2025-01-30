import numpy as np
from utils import load_from_csv

def analyze_results(file_path: str) -> dict:
    results = load_from_csv(file_path)
    mean_correct = np.mean(results)
    variance = np.var(results)
    probability_at_least_one = sum(1 for r in results if r > 0) / len(results)

    summary = {
        "Mean Correct": mean_correct,
        "Variance": variance,
        "Probability of At Least One Correct": probability_at_least_one
    }
    return summary

if __name__ == "__main__":
    summary = analyze_results("outputs/simulation_results.csv")
    with open("outputs/analysis_summary.txt", "w") as f:
        for key, value in summary.items():
            f.write(f"{key}: {value}\n")