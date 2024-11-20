import requests
import random

# API website: https://opentdb.com/api_config.php

def print_question(question_data):
    print(f"Question: {question_data['question']}")
    print(f"Difficulty: {question_data['difficulty']}")
    print(f"Category: {question_data['category']}")

    # Shuffle the answer choices to randomize the order
    answers = question_data['incorrect_answers'] + [question_data['correct_answer']]
    random.shuffle(answers)

    for i, answer in enumerate(answers):
        print(f"{i+1}. {answer}")
    
    return answers

def main():
    response = requests.get("https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=multiple")

    if(not response.ok):
        print("Error while retrieving questions, please try again later...")
        return
    
    data = response.json()

    for question_data in data['results']:
        answers = print_question(question_data)

        # Get user's answer
        user_answer = int(input("Enter your answer (1, 2, 3, or 4): ")) - 1
        selected_answer = answers[user_answer]

        # Check if the answer is correct
        if selected_answer == question_data['correct_answer']:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is: {question_data['correct_answer']}")

if __name__ == '__main__':
    main()