import os
import json


def print_scores(directory):

    for filename in os.listdir(directory):

        filepath = os.path.join(directory, filename)

        # print(filepath)
        if filepath.endswith('.json'):
            with open(filepath, "r") as f:
                students = json.load(f)

            subjects = {}

            for student in students:

                for subject, score in student.items():

                    subjects.setdefault(subject, []).append(score)

            for subject, scores in subjects.items():

                minimum = min(scores)
                maximum = max(scores)
                average = sum(scores) / len(scores)

                print(
                    f"{subject}: "
                    f"min {minimum}, "
                    f"max {maximum}, "
                    f"average {average:.1f}"
                )



print_scores(
    "/Users/sina/Desktop/mentoring_data/50-python-workout_AI_sessions/23"
)