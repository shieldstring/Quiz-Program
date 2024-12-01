import random
from colorama import Fore, Style
from tabulate import tabulate

def add_questions():
    """
    Allows admin to add 10 questions and their answers to the quiz.
    Returns a dictionary of questions and answers.
    """
    questions = {}
    print("Enter 10 questions and their answers:")
    for i in range(1, 11):
        question = input(f"Question {i}: ").strip()
        answer = input(f"Answer {i}: ").strip()
        questions[question] = answer
    return questions

def ask_question(question, correct_answer):
    """
    Asks a question and validates the user's answer.
    Returns True if the answer is correct, False otherwise.
    """
    while True:
        user_answer = input(f"{question} ").strip()
        if user_answer:
            if user_answer.lower() == correct_answer.lower():
                print(Fore.GREEN + "Correct!" + Style.RESET_ALL)
                return True
            else:
                print(Fore.RED + "Wrong!" + Style.RESET_ALL)
                return False
        else:
            print("Answer cannot be empty. Please try again.")

def run_quiz(questions):
    """
    Executes the quiz for a single user. 
    Returns the user's name and their score.
    """
    print("\nStarting the quiz!")
    user_name = input("Enter your name: ").strip()
    while not user_name:
        print("Name cannot be empty. Please try again.")
        user_name = input("Enter your name: ").strip()

    total_questions = len(questions)
    while True:
        try:
            num_questions = int(input(f"How many questions would you like to answer? (1-{total_questions}): "))
            if 1 <= num_questions <= total_questions:
                break
            else:
                print(f"Please enter a number between 1 and {total_questions}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    questions_list = list(questions.items())
    random.shuffle(questions_list)
    selected_questions = questions_list[:num_questions]

    score = 0
    correct_answers = []
    incorrect_answers = []

    for question, correct_answer in selected_questions:
        if ask_question(question, correct_answer):
            score += 1
            correct_answers.append(question)
        else:
            incorrect_answers.append((question, correct_answer))

    percentage = (score / num_questions) * 100
    print(f"\n{user_name}, you scored {score}/{num_questions} ({percentage:.2f}%).")

    # Show feedback
    print("\nQuiz Feedback:")
    if correct_answers:
        print("\nCorrectly Answered Questions:")
        for q in correct_answers:
            print(f"- {q}")

    if incorrect_answers:
        print("\nIncorrectly Answered Questions:")
        for q, a in incorrect_answers:
            print(f"- {q} (Correct Answer: {a})")

    return user_name, score

def display_results(user_scores):
    """
    Displays the results summary for all users.
    """
    print("\nResults Summary:")
    table = [[user['name'], user['score']] for user in user_scores]
    print(tabulate(table, headers=["Name", "Score"], tablefmt="grid"))

    highest_score = max(user_scores, key=lambda x: x['score'])
    average_score = sum(user['score'] for user in user_scores) / len(user_scores)
    
    print(f"\nHighest Scorer: {highest_score['name']} with {highest_score['score']}")
    print(f"Average Score: {average_score:.2f}")

def main():
    """
    Main function to execute the quiz program.
    """
    print("Welcome to the Quiz Program!")
    questions = add_questions()
    user_scores = []
    
    while True:
        user_name, score = run_quiz(questions)
        user_scores.append({'name': user_name, 'score': score})
        
        another = input("\nDoes another user want to take the quiz? (yes/no): ").strip().lower()
        if another != 'yes':
            break

    display_results(user_scores)

if __name__ == "__main__":
    main()
