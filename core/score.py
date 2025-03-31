import os

SCORE_FILE = "score_history.txt"


def save_score(score):
    with open(SCORE_FILE, "a") as file:
        file.write(f"{score}\n")


def load_scores():
    if not os.path.exists(SCORE_FILE):
        return []
    with open(SCORE_FILE, "r") as file:
        return [int(line.strip()) for line in file.readlines() if line.strip().isdigit()]


def get_top_scores(limit=5):
    scores = load_scores()
    scores.sort(reverse=True)
    return scores[:limit]
