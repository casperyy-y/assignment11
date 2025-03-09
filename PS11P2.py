exam_scores = [85, 90, 78, 88, 92, 76, 95, 89, 84, 91]

def display_names_and_scores(names, scores):
    print("\nList of Last Names and Exam Scores:")
    for i in range(len(names)):
        print(f"{names[i]} - {scores[i]}")

display_names_and_scores(last_names, exam_scores)
