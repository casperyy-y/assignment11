def find_highest(names, scores):
    highest_score = max(scores)
    index = scores.index(highest_score)
    print(f"\nHighest Score: {highest_score} by {names[index]}")

def find_lowest(names, scores):
    lowest_score = min(scores)
    index = scores.index(lowest_score)
    print(f"\nLowest Score: {lowest_score} by {names[index]}")

find_highest(last_names, exam_scores)
find_lowest(last_names, exam_scores)
