import matplotlib.pyplot as plt
import numpy as np
from utils import load_from_csv

def plot_histogram(file_path: str):
    results = load_from_csv(file_path)
    plt.hist(results, bins=range(0, max(results) + 2), density=True, alpha=0.7)
    plt.xlabel("Number of Correct Matches")
    plt.ylabel("Probability")
    plt.title("Distribution of Correct Hat Matches")
    plt.savefig("outputs/visualizations/histogram.png")
    plt.close()

def plot_probability_curve(file_path: str):
    results = load_from_csv(file_path)
    values, counts = np.unique(results, return_counts=True)
    probabilities = counts / len(results)

    plt.plot(values, probabilities, marker="o", linestyle="-")
    plt.xlabel("Number of Correct Matches")
    plt.ylabel("Probability")
    plt.title("Probability Distribution of Hat Matches")
    plt.savefig("outputs/visualizations/probability_curve.png")
    plt.close()

if __name__ == "__main__":
    plot_histogram("outputs/simulation_results.csv")
    plot_probability_curve("outputs/simulation_results.csv")