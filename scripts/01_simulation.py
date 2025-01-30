import random
from utils import save_to_csv

def simulate_check_hat(N: int, num_people: int) -> list:
    results = []
    for _ in range(N):
        hats = list(range(num_people))
        random.shuffle(hats)
        correct_count = sum(1 for i in range(num_people) if hats[i] == i)
        results.append(correct_count)
    return results

if __name__ == "__main__":
    num_people = 100
    num_trials = 10000

    results = simulate_check_hat(num_trials, num_people)
    save_to_csv(results, "outputs/simulation_results.csv")